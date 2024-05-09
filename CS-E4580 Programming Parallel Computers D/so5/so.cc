#include <algorithm>
#include <cmath>
#include <vector>
#include <omp.h>

typedef unsigned long long data_t;


void parallel_quicksort(int threads, int n, data_t *data) {

    if (n < 2) {
     return;
    }
    
    if (threads <= 0) { 
        std::sort(data, data+n);
        return;
    }
    
    auto p1 = data[n/2];
    auto p2 = data[0];
    auto p3 = data[n-1];
    auto pivot = p1 + p2 + p3 - std::max(p1, std::max(p2, p3)) - std::min(p1, std::max(p2, p3));
    
    auto *left = data;
    auto *right = data + n - 1;

    while (left <= right) {
        while (*left < pivot) {
      		left++;
        }
        while (*right > pivot) {
             	right--;
        }
        
        if (left <= right) {
        
            auto temp = *left;
            
            *left = *right;
            *right = temp;
            
            left++;
            right--;
        }
    }
    
    #pragma omp task
    {
    parallel_quicksort((threads - 1), (right - data + 1), data);
    }
    
    #pragma omp task
    {
    parallel_quicksort((threads - 1), (n - (left - data)), left);
    }
}

void psort(int n, data_t *data) {
    // FIXME: Implement a more efficient parallel sorting algorithm for the CPU,
    // using the basic idea of quicksort.
    //std::sort(data, data + n);
    
    int threads = std::log2(omp_get_max_threads()) * 2;
    #pragma omp parallel 
    {
        #pragma omp single 
        {
            parallel_quicksort(threads, n, data);
    	}
    }
}
