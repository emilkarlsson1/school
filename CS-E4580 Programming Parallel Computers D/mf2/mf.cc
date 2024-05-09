/*
This is the function you need to implement. Quick reference:
- input rows: 0 <= y < ny
- input columns: 0 <= x < nx
- element at row y and column x is stored in in[x + y*nx]
- for each pixel (x, y), store the median of the pixels (a, b) which satisfy
  max(x-hx, 0) <= a < min(x+hx+1, nx), max(y-hy, 0) <= b < min(y+hy+1, ny)
  in out[x + y*nx].
*/
#include <vector>
#include <algorithm>

void mf(int ny, int nx, int hy, int hx, const float *in, float *out) {
    #pragma omp parallel for schedule(static,1)
    for (int row = 0; row < ny; row++) {
        	for (int column = 0; column < nx; column++) {

		    int jmin = std::max(row - hy, 0);
		    int imin = std::max(column - hx, 0);
		    int jmax = std::min(row + hy, ny - 1);
		    int imax = std::min(column + hx, nx - 1);

		    std::vector<float> idata((imax - imin + 1) * (jmax - jmin + 1));
		    idata.clear();

		    for (int j = jmin; j <= jmax; j++) {
		        for (int i = imin; i <= imax; i++) {
		            idata.push_back(in[i + nx * j]);
		        }
            	    }

		    int size = idata.size();
		    int middle_num = size / 2;

		    std::nth_element(idata.begin(), idata.begin() + middle_num, idata.end());

		    float median = idata[middle_num];

		    if (size % 2 == 1) {
		        out[column + nx * row] = median;
		    } else {
		        std::nth_element(idata.begin(), idata.begin() + middle_num - 1, idata.end());
		        out[column + nx * row] = (0.5) * (median + idata[middle_num - 1]);
		    }
        	}
    }
}


