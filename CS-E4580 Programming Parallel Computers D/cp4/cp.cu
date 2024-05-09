/*
This is the function you need to implement. Quick reference:
- input rows: 0 <= y < ny
- input columns: 0 <= x < nx
- element at row y and column x is stored in data[x + y*nx]
- correlation between rows i and row j has to be stored in result[i + j*ny]
- only parts with 0 <= j <= i < ny need to be filled
*/

#include <vector>
#include <iostream>
#include <cuda_runtime.h>


static inline void check(cudaError_t err, const char* context) {
    if (err != cudaSuccess) {
        std::cerr << "CUDA error: " << context << ": "
            << cudaGetErrorString(err) << std::endl;
        std::exit(EXIT_FAILURE);
    }
}

#define CHECK(x) check(x, #x)

static inline int divup(int a, int b) {

    return (a + b - 1)/b;
}

__global__ void correlate_kernel(int num_rows, int num_cols, const float* data, float* result) {
    int i = threadIdx.x + blockIdx.x * blockDim.x;
    int j = threadIdx.y + blockIdx.y * blockDim.y;

    if (i >= num_rows || j >= num_rows)
        return;

    float sum = 0;
    for (int k = 0; k < num_cols; k++){
        sum += data[k + i * num_cols] * data[k + j * num_cols];
    }
    result[j + i * num_rows] = sum;
}

void correlate(int ny, int nx, const float *data, float *result) {

    float *normalized_data = (float *)malloc(sizeof(float) * ny * nx);
    for (int i = 0; i < ny; i ++) {
        float row_sum = 0;
        
        for (int j = 0; j < nx; j ++) {
            row_sum += data[j + i * nx];
        }
        float row_mean = row_sum / nx;

        float row_square_sum = 0;
        
        for (int j = 0; j < nx; j ++) {
            float x = data[j + i * nx] - row_mean;
            normalized_data[j + i * nx] = x;
            row_square_sum += x * x;
        }

        row_square_sum = sqrt(row_square_sum);
        for(int j = 0; j < nx; j++) {
            normalized_data[j + i * nx] /= row_square_sum;
        }
    }

 
    float* d_norm_data = NULL;
    float* d_result = NULL;
    CHECK(cudaMalloc((void**)&d_norm_data, ny * nx * sizeof(float)));
    CHECK(cudaMalloc((void**)&d_result, ny * ny * sizeof(float)));
    CHECK(cudaMemcpy(d_norm_data, normalized_data, ny * nx * sizeof(float), cudaMemcpyHostToDevice));


    dim3 block_size(32, 32);
    dim3 grid_size(divup(ny, block_size.x), divup(ny, block_size.y));
    correlate_kernel<<<grid_size, block_size>>>(ny, nx, d_norm_data, d_result);
    CHECK(cudaGetLastError());


    CHECK(cudaMemcpy(result, d_result, ny * ny * sizeof(float), cudaMemcpyDeviceToHost));
    CHECK(cudaFree(d_norm_data));
    CHECK(cudaFree(d_result));

    free(normalized_data);
}
