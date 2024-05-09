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

static inline int divup(int a, int b) {
    return (a + b - 1)/b;
}

static inline int roundup(int a, int b) {
    return divup(a, b) * b;
}

static inline void check(cudaError_t err, const char* context) {
    if (err != cudaSuccess) {
        std::cerr << "CUDA error: " << context << ": "
            << cudaGetErrorString(err) << std::endl;
        std::exit(EXIT_FAILURE);
    }
}

#define CHECK(x) check(x, #x)

//from slides
__global__ void correlate_kernel(int nx, int ny, int nx_p, int ny_p, float* transposed, float* result) {
   
    int ia = threadIdx.x;
    int ja = threadIdx.y;
    int ic = blockIdx.x;
    int jc = blockIdx.y;

    if (ic > jc) {
        for (int ib = 0; ib < 8; ib++) {
            for (int jb = 0; jb < 8; jb++) {
                int i = ic * 64 + ib * 8 + ia;
                int j = jc * 64 + jb * 8 + ja;
                if (i < ny && j < ny) {
                	result[j + i*ny] = 0.0;
                }
            }
        }
    } else {
	    float v[8][8];
	    for (int ib = 0; ib < 8; ib++) {
		for (int jb = 0; jb < 8; jb++) {
		    v[ib][jb] = 0;
		}
	    }
	    
	    for (int k = 0; k < nx; k++) {
		float x[8];
		float y[8];
		for (int ib = 0; ib < 8; ib++) {
		    int i = ic * 64 + ib * 8 + ia;
		    x[ib] = transposed[ny_p * k + i];
		}
		
		for (int jb = 0; jb < 8; jb++) {
		    int j = jc * 64 + jb * 8 + ja;
		    y[jb] = transposed[ny_p * k + j];
		}
		
		for (int ib = 0; ib < 8; ib++) {
		    for (int jb = 0; jb < 8; jb++) {
		        v[ib][jb] += x[ib] * y[jb];
		    }
		}
	    }
	    
	    for (int ib = 0; ib < 8; ib++) {
		for (int jb = 0; jb < 8; jb++) {
		    int i = ic * 64 + ib * 8 + ia;
		    int j = jc * 64 + jb * 8 + ja;
		    if (i < ny && j < ny) {
		    	result[j + i*ny] = v[ib][jb];
		    }
		}
	    }
    }
}

__global__ void correlate_kernel_transpose(int nx, int ny, int nx_p, int ny_p, float* transposed, float* normalized) {
    int ja = threadIdx.x; 
    int i = blockIdx.y; 

    for (int jb = 0; jb < nx_p; jb += 64) 
    {
        int j = jb + ja;
        transposed[ny_p * j + i] = (i < ny && j < nx) ? normalized[nx * i + j] : 0;
    }
}

__global__ void gpu_normalize(int nx, int ny, int nx_p, int ny_p, float* normalized, float* data) {

    int ja = threadIdx.y;
    int i = blockIdx.y;

    int y = i * 64 + ja;
    if (y < ny) {
        float row_sum = 0.0;
        float row_square_sum = 0.0;
        
        for (int x = 0; x < nx; x++) {   
            row_sum += data[x + y*nx];
        }
        
        float rwo_avg = row_sum/nx;
        for (int x = 0; x < nx; x++) {   
            float item = data[x + y*nx]-rwo_avg;
            normalized[x + y*nx] = item;
            row_square_sum += pow(item, 2);
        }
        
        float root_square_sum = sqrt(row_square_sum);
        for (int x = 0; x < nx; x++) {
            normalized[x + y*nx] /= root_square_sum;         
        }
    }
}


void correlate(int ny, int nx, const float* data, float* result) {
    
    int nx_p = roundup(nx, 64);
    int ny_p = roundup(ny, 64);

    //initialize pointers to null
    float* dGPU = NULL;
    float* dGPU_raw = NULL;
    float* dGPU_norm = NULL;
    float* rGPU = NULL;


    const int input_sz = nx_p * ny_p * sizeof(float);
    const int mtx_sz = nx * ny * sizeof(float);
    const int out_sz = ny * ny * sizeof(float);


    CHECK(cudaMalloc((void**)&dGPU, input_sz));
    CHECK(cudaMalloc((void**)&dGPU_raw, mtx_sz));
    CHECK(cudaMalloc((void**)&dGPU_norm, mtx_sz));
    CHECK(cudaMalloc((void**)&rGPU, out_sz));
    CHECK(cudaMemcpy(dGPU_raw, data, mtx_sz, cudaMemcpyHostToDevice));

  
    {
        dim3 dimBlock(1, 64);
        dim3 dimGrid(1, ny_p/64);
        gpu_normalize<<<dimGrid, dimBlock>>>(nx, ny, nx_p, ny_p, dGPU_norm, dGPU_raw);
        CHECK(cudaGetLastError());
    }

    {
        dim3 dimBlock(64, 1);   
        dim3 dimGrid(1, ny_p);  
        correlate_kernel_transpose<<<dimGrid, dimBlock>>>(nx, ny, nx_p, ny_p, dGPU, dGPU_norm);
        CHECK(cudaGetLastError());
    }

    {
        dim3 dimBlock(8, 8);
        dim3 dimGrid(ny_p / 64, ny_p / 64); 
        correlate_kernel<<<dimGrid, dimBlock>>>(nx, ny, nx_p, ny_p, dGPU, rGPU);
        CHECK(cudaGetLastError());
    }


    CHECK(cudaMemcpy(result, rGPU, out_sz, cudaMemcpyDeviceToHost));
    CHECK(cudaFree(dGPU));
    CHECK(cudaFree(dGPU_raw));
    CHECK(cudaFree(dGPU_norm));
    CHECK(cudaFree(rGPU));
}
