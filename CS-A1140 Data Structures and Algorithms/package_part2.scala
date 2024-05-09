// Scala 2 (DO NOT EDIT OR REMOVE THIS LINE!!!)

/* Author: Tommi Junttila, Aalto University.
 * Only for the use on the Aalto course CS-A1140.
 * Redistribution not allowed.
 */

package object peakFinder {
  /**
   * An auxiliary helper function used in the unit tests.
   * Checks whether the given index is a peak in the array arr.
   * You may use it as well if you wish (but you don't have to).
   */
  def isPeak[T](arr: Array[T], index: Int)(implicit ev: T => Ordered[T]): Boolean = {
    require(arr.nonEmpty)
    val n = arr.length
    require(0 <= index && index < n)
    if(index == 0)
      n == 1 || arr(index) >= arr(index+1)
    else if(index == n-1)
      arr(index) >= arr(index-1)
    else
      arr(index) >= arr(index-1) && arr(index) >= arr(index+1)
  }

  /**
   * Returns the index of a peak in the array arr.
   * Works in time O(n), where n is the number of elements in arr.
   */
  def solveLinear[T](arr: Array[T])(implicit ev: T => Ordered[T]): Int = {
    require(arr.nonEmpty)
    // The number of elements in the array
    val n = arr.length
    // Only one element? Then it is a peak.
    if(n == 1)
      return 0
    // Is the first element (with no "left" neighbour) a peak?
    if(arr(0) >= arr(1))
      return 0
    // For each of the n-2 "internal" elements, check if it is a peak
    var i = 1
    while(i < n-1) {
      // Is arr(i) at least as large as its "left" and "right" neighbours?
      if(arr(i) >= arr(i-1) && arr(i) >= arr(i+1))
        return i;
      i += 1
    }
    // Is the last element (with no "right" neighbour) a peak?
    if(arr(n-1) >= arr(n-2))
      return n-1
    assert(false, "Should never enter this line as a peak always exists")
    return -1 // This is only for type checking
  }

  /**
   * Returns the index of a peak in the array arr.
   * Should works in time O(log n) and use at most 3*log2(n) comparisons,
   * where n is the number of elements in arr.
   * Note: The "implicit ev" allows one to use the comparison operators
   * <, <=, ==, >=, and > on the type T if they are available
   * (see solveLinear above).
   * Thus arr could be an array of integers, floats, or doubles, for instance.
   */
  def solveLog[T](arr: Array[T])(implicit ev: T => Ordered[T]): Int = {
    require(arr.nonEmpty)
    val n = arr.length

    if (n == 1) {
      return 0
    }
    if(arr(0) >= arr(1))
      return 0
    if(arr(n-1) >= arr(n-2))
      return n-1

    
    var i = 1
    var low = 0
    var high = arr.length -1
    while (low < high) {
      val mid = low + (high-low) / 2
      if (arr(mid) > arr (mid+1)) {
        high = mid
      } else {
        low = mid+1
      }
    }
    return low    
  }
}
