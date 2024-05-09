/*
This is the function you need to implement. Quick reference:
- input rows: 0 <= y < ny
- input columns: 0 <= x < nx
- element at row y and column x is stored in data[x + y*nx]
- correlation between rows i and row j has to be stored in result[i + j*ny]
- only parts with 0 <= j <= i < ny need to be filled
*/
#include <vector>
#include <cmath>

void correlate(int ny, int nx, const float* data, float* result) {

	std::vector<double> idata(nx * ny);

	// Loop over each row
	for (int row = 0; row < ny; row++) {
		// Calculate the mean of this row
		double row_sum = 0;

		for (int column = 0; column < nx; column++) {
			row_sum += data[column + row * nx];
		}
		double row_mean = row_sum / nx;


		double row_square_sum = 0;

		// Calculate the standard deviation of this row
		for (int column = 0; column < nx; column++) {

			double x = data[column + row * nx] - row_mean;

			idata[column + row * nx] = x;
			row_square_sum += x * x;
		}
		double row_standard_dev = sqrt(row_square_sum);

		// Normalize the row
		for (int column = 0; column < nx; column++) {
			idata[column + row * nx] /= row_standard_dev;
		}
	}

	// Loop over all pairs of rows

	for (int i = 0; i < ny; i++) {
		for (int j = i; j < ny; j++) {
			double sum[4] = { 0 };
			double dev = nx / 4;
			for (int k = 0; k < dev; k++) {
				for (int z = 0; z < 4; z++) {
					sum[z] += idata[i * nx + z + 4* k] * idata[j * nx + z + 4 * k];
				}
			}
			// Calculate the correlation coefficient between rows i and j
			double dot_product = 0;
			double pros = nx % 4;
			for (int e = 0; e < pros; e++) {
				dot_product += idata[i * nx + (nx - pros) + e] * idata[j * nx + (nx - pros) + e];	
			}
			
			for (int q = 0; q < 4; q++) {
				dot_product += sum[q];
			}


			result[j + i * ny] = static_cast<float>(dot_product);
		}
	}


}