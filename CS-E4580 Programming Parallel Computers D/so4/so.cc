#include <algorithm>
#include <cmath>
#include <vector>
#include <omp.h>


typedef unsigned long long data_t;


void merge_sort(int threads, int n, data_t* data) {
    if (threads <= 0) {
        std::sort(data, data + n);
        return;
    }
    
    int m = (n + 1) / 2;
    #pragma omp task
    {
        merge_sort(threads - 1, m, data);
    }
    #pragma omp task
    {
        merge_sort(threads - 1, n - m, data + m);
    }
    #pragma omp taskwait
    {
        std::inplace_merge(data, data + m, data + n);	
    }
}

void psort(int n, data_t *data) {
    // FIXME: Implement a more efficient parallel sorting algorithm for the CPU,
    // using the basic idea of merge sort.
    //std::sort(data, data + n);
    
    int threads = std::log2(omp_get_max_threads()) * 2;
    #pragma omp parallel 
    {
        #pragma omp single 
        {
            merge_sort(threads, n, data);
    	}
    }
}
