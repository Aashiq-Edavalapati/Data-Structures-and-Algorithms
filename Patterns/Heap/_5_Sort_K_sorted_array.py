# Link: https://takeuforward.org/data-structure/sort-k-sorted-array

"""
    @question:
        Given an array arr[] and a number k . The array is sorted in a way that every element is at max k distance away from it sorted position. It means if we completely sort the array, then the index of the element can go from i - k to i + k where i is index in the given array. Our task is to completely sort the array.

        Examples
            Input :  arr = [6, 5, 3, 2, 8, 10, 9], k = 3  
            Output :  [2, 3, 5, 6, 8, 9, 10]  
            Explanation :  The element 2 was at index 3, it moved to index 0. The element 3 was at index 2, it moved to index 1. The element 5 moved from index 1 to index 2. The element 6 moved from index 0 to index 3. The rest (8, 9, 10) were near their correct spots and shifted slightly.

        ----------------------------------------------------------

            Input :  arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2  
            Output :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
            Explanation :  The element 2 moved from index 3 to index 1. The element 3 moved from index 4 to index 2. The element 4 moved from index 1 to index 3. The element 5 moved from index 2 to index 4. All others remained in or near their correct positions.
"""
from typing import List
import heapq


"""
    @intuition:
        Since, the elements are moved at most k elements from it's actual position in the sorted array:
            => The smallest element will definitely be in the first k elements,
                 1st element will definitely be in the first k + 1 elementst, etc....
                 ith element will definitely be in the first k + i elements
            => We maintain a sliding window of size k and min heap to keep track of minimum in that window
"""
def sortKSortedArray(arr: List[int], k: int) -> List[int]:
    minHeap = []
    n = len(arr)
    for i in range(k + 1):
        heapq.heappush(minHeap, arr[i])
    
    sortedArr = []
    for i in range(k + 1, n):
        sortedArr.append(heapq.heappop(minHeap))
        heapq.heappush(minHeap, arr[i])
    
    while minHeap:
        sortedArr.append(heapq.heappop(minHeap))
    
    return sortedArr

if __name__ == '__main__':
    testCases = [
        ([6, 5, 3, 2, 8, 10, 9], 3), # [2, 3, 5, 6, 8, 9, 10]
        ([1, 4, 5, 2, 3, 6, 7, 8, 9, 10], 2), # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    ]

    for i, testCase in enumerate(testCases):
        arr, k = testCase
        print(f"TestCase {i}:- i/p: arr={arr}, k={k}; o/p: {sortKSortedArray(arr, k)}")