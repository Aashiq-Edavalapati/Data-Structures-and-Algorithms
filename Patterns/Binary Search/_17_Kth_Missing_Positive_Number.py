from typing import List

# -----------------------------------------------------------------------------
# Problem: Kth Missing Positive Number
# -----------------------------------------------------------------------------
#
# @question:
#   Given a sorted array of positive integers `arr` and an integer `k`, return
#   the `k`-th positive integer that is missing from this array.
#
# -----------------------------------------------------------------------------
#
# @pattern: Discard Half
#
# -----------------------------------------------------------------------------
#
# @method:
#    Binary Search on Answer
#   1. Let `missing(i)` = arr[i] - (i + 1), which gives the number of missing
#      integers up to index i.
#   2. Use binary search to find the smallest index where missing(i) >= k.
#   3. The answer is `left + k`, where `left` is the number of elements in arr
#      that are <= the kth missing number.
#
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ==============================================================================
#
# @intuition:
#       The array is sorted! => Immediately, Binary Search should strike to our mind
#       But, the answer we are searching for is not an element of the array!
#       Then, how do we apply binary search? => Binary Search over answer!
#       Once we figure that out, what's next? => Search Space
#       Obviously, the answer is going to lie between [1, max(arr)]
#       After finding the search space, we have to think of the condition to eliminate the appropriate half of the search space
#       Consider the array where no number is missing! Here, `k`th number will be at the index `k - 1`
#       => Number of integers missing up to index i = arr[i] - (i + 1)

def kthMissingNum(arr: List[int], k: int) -> int:
    """
    Finds the k-th missing positive integer from a sorted list `arr`.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # Number of missing integers before arr[mid]
        missing_count = arr[mid] - (mid + 1)

        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1
    
    # After binary search, `left` is the count of elements <= answer
    return left + k

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    test_cases = [
        ([2, 3, 4, 7, 11], 5),   # Expected: 9
        ([1, 2, 3, 4], 2),       # Expected: 6
        ([5, 6, 7, 8, 9], 4)     # Expected: 4
    ]

    for i, (arr, k) in enumerate(test_cases, start=1):
        print(f"Test Case {i}: kthMissingNum = {kthMissingNum(arr, k)}")
