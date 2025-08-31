# -----------------------------------------------------------------------------
# Problem: Row with Maximum 1s in a Binary Matrix
# -----------------------------------------------------------------------------
#
# @question:
#   Given a binary matrix (0s and 1s), where each row is sorted,
#   return the row that contains the maximum number of 1s.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search in Rows
#
# -----------------------------------------------------------------------------
# @method:
#   1. In each row, use binary search to find the first '1'.
#   2. Count of 1s in that row = (total_columns - first_index_of_1).
#   3. Track the row with the maximum count.
#
# Time Complexity: O(n log m)  (n = rows, m = columns)
# Space Complexity: O(1)
# ==============================================================================

def count1s(arr):
    left, right = 0, len(arr) - 1
    ans = len(arr)  # if no '1' exists
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == 1:
            ans = mid     # found a '1', try to move left for first '1'
            right = mid - 1
        else:
            left = mid + 1

    return len(arr) - ans  # number of 1s in this row


def rowWithMax1s(matrix):
    n = len(matrix)
    m = len(matrix[0])

    max1s = 0
    rowIndex = -1
    for i in range(n):
        count = count1s(matrix[i])
        if count > max1s:
            max1s = count
            rowIndex = i

    return rowIndex, max1s   # returns row index + number of 1s


# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    testCases = [
        ([[0,0,1,1,1], 
          [0,0,0,0,0], 
          [0,1,1,1,1], 
          [0,0,0,0,0], 
          [0,1,1,1,1]]),
        
        ([[0,0,0,0], 
          [0,0,0,1], 
          [0,1,1,1]]),

        ([[0,0,0], 
          [0,0,0]])
    ]

    i = 0
    for matrix in testCases:
        row, count = rowWithMax1s(matrix)
        print(f'TestCase {i}: Row {row} has max {count} ones')
        i += 1
