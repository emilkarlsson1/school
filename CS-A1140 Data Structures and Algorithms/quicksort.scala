// Scala 2 (DO NOT EDIT OR REMOVE THIS LINE!!!)

/* Author: Tommi Junttila, Aalto University.
 * Only for the use on the Aalto course CS-A1140.
 * Redistribution not allowed.
 */

package sorts

object quicksort {
  def swap(a: Array[Int], i: Int, j: Int): Unit = {
    val t = a(i); a(i) = a(j); a(j) = t
  }

  def median(a: Array[Int], i1: Int, i2: Int, i3: Int): Int = {
    if(a(i1) <= a(i2)) {
      if(a(i2) <= a(i3)) i2
      else if(a(i3) <= a(i1)) i1
      else i3
    } else {
      if(a(i1) <= a(i3)) i1
      else if(a(i3) <= a(i2)) i2
      else i3
    } 
  }

  def partition(a: Array[Int], lo: Int, hi: Int): Int = {
    val pivotIndex = median(a, lo, (lo+hi)/2, hi)
    val pivot = a(pivotIndex)
    swap(a, pivotIndex, hi)
    var i = lo - 1
    var j = lo
    while (j < hi) {
      if (a(j) <= pivot) { i += 1; swap(a, i, j) }
      j += 1
    }
    swap(a, i + 1, hi)
    i + 1
  }

  /**
   * Sort the array a by using sequential quicksort.
   * Small subarrays (those below threshold) are sorted with insertion sort.
   */
  def sort(a: Array[Int], threshold: Int = 32): Unit = {
    def _quicksort(lo: Int, hi: Int): Unit = {
      if(hi - lo < threshold) insertionsort.sort(a, lo, hi)
      else {
        val j = partition(a, lo, hi)
        if (lo < j - 1) _quicksort(lo, j - 1)
        if (j + 1 < hi) _quicksort(j + 1, hi)
      }
    }
    if (a.length >= 2) _quicksort(0, a.length - 1)
  }

  /**
   * Sort the array a by using parallel quicksort.
   * Small subarrays (those below threshold) are sorted with insertion sort.
   */
  def sortPar(a: Array[Int], threshold: Int = 32): Unit = {
    def merge(a: Array[Int], aux: Array[Int],
            start: Int, mid: Int, end: Int): Unit = {
    var (i, j, dest) = (start, mid, start)
    while (i < mid && j <= end) {
      if (a(i) <= a(j)) { 
        aux(dest) = a(i); i += 1 
      }
      else { 
        aux(dest) = a(j); j += 1 
      }
      dest += 1
    }
    while (i < mid) { 
      aux(dest) = a(i); i += 1; dest += 1 
    }  
    while (j <= end) { 
      aux(dest) = a(j); j += 1; dest += 1 
    } 
    dest = start 
    while (dest <= end) { 
      a(dest) = aux(dest); dest += 1 
    }
  }
    if (a.length <= 1) return
    val aux = new Array[Int](a.length)
    def _parallel(lo: Int, hi: Int): Unit = {
      if (hi - lo < threshold) 
        insertionsort.sort(a, lo, hi)
      else {
        val mid = lo + (hi-lo) /2
        par.parallel(_parallel(lo, mid), _parallel(mid+1, hi))
        merge(a, aux, lo, mid +1, hi)
      }

    }
    if (a.length >= 2) 
      _parallel(0, a.length - 1)
  }
}
