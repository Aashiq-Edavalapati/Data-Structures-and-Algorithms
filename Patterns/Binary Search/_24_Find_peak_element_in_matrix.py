# -----------------------------------------------------------------------------
# Problem: Find a Peak Element in a 2D Matrix
# -----------------------------------------------------------------------------
#
# @question:
#   A peak element in a 2D matrix is an element that is strictly greater than
#   the element above and below it (if they exist).
#   Return the position [row, col] of any one peak.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Matrix Rows
#
# -----------------------------------------------------------------------------
# @method:
#   1. Apply binary search on rows.
#   2. In the middle row, find the column index of the maximum element.
#   3. Compare it with the element above and below:
#       - If it's a peak → return it.
#       - If the element above is bigger → move search to top half.
#       - If the element below is bigger → move search to bottom half.
#
# Time Complexity: O(n log m)   (binary search on rows + scan each row for max)
# Space Complexity: O(1)
# ==============================================================================

def peakInMat(matrix):
    n = len(matrix)
    m = len(matrix[0])
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Find column index of maximum element in this row
        maxEl, maxi = -1, -1
        for j in range(m):
            if matrix[mid][j] > maxEl:
                maxEl = matrix[mid][j]
                maxi = j

        # Compare with element above and below
        up = matrix[mid - 1][maxi] if mid > 0 else -1
        down = matrix[mid + 1][maxi] if mid < n - 1 else -1

        if up <= maxEl and down <= maxEl:
            return [mid, maxi]  # found peak
        elif up > maxEl:
            right = mid - 1     # move upward
        else:
            left = mid + 1      # move downward

if __name__ == '__main__':
    testCases = [
        [[1,4,3],[6,7,8],[5,2,9]],   # Peak could be [2,2] (9)
        [[10,8,10,10],[14,13,12,11],[15,9,11,21],[16,17,19,20]]  # Peak [3,3] (20)
    ]

    i = 0
    for mat in testCases:
        print(f"TestCase {i}: Peak at {peakInMat(mat)}")
        i += 1
