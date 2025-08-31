# -----------------------------------------------------------------------------
# Problem: Median in a Row-wise Sorted Matrix
# -----------------------------------------------------------------------------
#
# @question:
#   You are given an m x n matrix where each row is sorted.
#   Find the median of all elements in the matrix.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Answer
#
# -----------------------------------------------------------------------------
# @method:
#   1. The median is the middle element if we sort all values.
#   2. Instead of flattening and sorting (O(m*n log(m*n))),
#      we use binary search on the possible value range:
#       - The smallest value = min(first elements of rows).
#       - The largest value  = max(last elements of rows).
#   3. For each mid-value, count how many numbers ≤ mid:
#       - Use upperBound (binary search) on each row.
#   4. If count <= required count (half of total elements),
#        move search to right half.
#      Else move to left half.
#   5. When loop ends, `left` will be the median.
#
# Time Complexity: O(m log(max-min) * log n)
#   - log(max-min) → binary search on value range
#   - log n per row for upperBound
# Space Complexity: O(1)
# ==============================================================================

def upperBound(arr, n, el):
    """
    Returns the index of the first element greater than 'el'.
    (Same as bisect_right in Python).
    """
    left, right = 0, n - 1
    ans = n
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > el:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


def getCount(matrix, m, n, el):
    """
    Counts how many numbers in the matrix are <= el
    by summing counts from each row.
    """
    count = 0
    for i in range(m):
        count += upperBound(matrix[i], n, el)
    return count


def median(matrix):
    """
    Finds the median of the row-wise sorted matrix.
    """
    m, n = len(matrix), len(matrix[0])

    # Search space = [min element, max element]
    left, right = float('inf'), float('-inf')
    for i in range(m):
        left = min(left, matrix[i][0])
        right = max(right, matrix[i][-1])

    reqCount = (m * n) // 2  # Half of total elements

    # Binary search on value range
    while left <= right:
        mid = left + (right - left) // 2
        count = getCount(matrix, m, n, mid)

        if count <= reqCount:
            left = mid + 1
        else:
            right = mid - 1

    return left  # left will point to median


# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    testCases = [
        ([[1,5,7,9,11],
          [2,3,4,8,9],
          [4,11,14,19,20],
          [6,10,22,99,100],
          [7,15,17,24,28]])
    ]

    i = 0
    for matrix in testCases:
        print(f'TestCase {i}: {median(matrix)}')
        i += 1
