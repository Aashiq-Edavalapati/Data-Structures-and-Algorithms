# -----------------------------------------------------------------------------
# Problem: Median of Two Sorted Arrays
# -----------------------------------------------------------------------------
#
# @question:
#   You are given two sorted arrays `arr1` and `arr2`.
#   Find the median of the two sorted arrays combined.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Answer
#   - Instead of merging arrays (O(n1+n2)), we use binary search.
#   - The idea is to partition both arrays such that:
#       - Left half has exactly (n1+n2+1)//2 elements
#       - All elements in left half ≤ all elements in right half
#
# -----------------------------------------------------------------------------
# @method (step-by-step):
#   1. Always binary search on the smaller array (to minimize search space).
#   2. For each mid1 in arr1, calculate mid2 = leftSize - mid1.
#   3. Define:
#        l1 = element just before mid1 in arr1 (or -inf if none)
#        r1 = element at mid1 in arr1 (or +inf if none)
#        l2 = element just before mid2 in arr2 (or -inf if none)
#        r2 = element at mid2 in arr2 (or +inf if none)
#   4. If partition is correct:
#        - l1 <= r2 and l2 <= r1
#        - then median depends on total length:
#            - odd length → max(l1, l2)
#            - even length → (max(l1, l2) + min(r1, r2)) / 2
#   5. If l1 > r2 → move search left (reduce mid1).
#      If l2 > r1 → move search right (increase mid1).
#
# Time Complexity: O(log(min(n1, n2)))
# Space Complexity: O(1)
# ==============================================================================

def median(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    # Always binary search on smaller array
    if n1 > n2: 
        return median(arr2, arr1)

    left, right = 0, n1
    leftSize = (n1 + n2 + 1) // 2  # size of left partition

    while left <= right:
        mid1 = left + (right - left) // 2
        mid2 = leftSize - mid1

        # Set boundary values
        l1, l2 = float('-inf'), float('-inf')
        r1, r2 = float('inf'), float('inf')

        if mid1 < n1: r1 = arr1[mid1]
        if mid2 < n2: r2 = arr2[mid2]
        if mid1 > 0: l1 = arr1[mid1 - 1]
        if mid2 > 0: l2 = arr2[mid2 - 1]

        # Check if partition is valid
        if l1 > r2:
            right = mid1 - 1  # move left
        elif l2 > r1:
            left = mid1 + 1   # move right
        else:
            # Found correct partition
            if (n1 + n2) % 2 == 1:
                return max(l1, l2)  # odd length
            else:
                return (max(l1, l2) + min(r1, r2)) / 2  # even length

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    testCases = [
        ([1,3,4,7,10,12], [2,3,6,15]),   # even total length
        ([1,3,4,7,10], [2,3,6,15]),      # odd total length
        ([2,4], [1,3,4]),                # overlapping values
        ([1,2], [3,4])                   # disjoint arrays
    ]

    i = 0
    for arr1, arr2 in testCases:
        print(f'TestCase {i}: {median(arr1, arr2)}')
        i += 1
