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
#   - The array is sorted, so we can reason about how many numbers are missing
#     up to a certain index and cut the search space in half each step.
#
# -----------------------------------------------------------------------------
#
# @method:
#   1. Define missing(i) = arr[i] - (i + 1).
#        - This tells how many positive numbers are missing before index i.
#   2. We want the smallest index `i` such that missing(i) >= k.
#   3. Use binary search:
#        - If missing(mid) < k, answer is to the right (move left pointer).
#        - Else, answer is to the left (move right pointer).
#   4. After search, `left` is the count of numbers in arr that are <= the answer.
#      So final answer = left + k.
#
# Time Complexity: O(log N)
# Space Complexity: O(1)
# ==============================================================================
#
# @intuition (simple):
#   - Sorted array → binary search comes to mind.
#   - But we are not searching for an element in arr, instead for the kth missing number.
#   - Trick: Count how many numbers are missing until each index.
#   - Use binary search to find where kth missing fits in.
#   - Formula at the end: answer = left + k

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
            # Not enough missing yet → go right
            left = mid + 1
        else:
            # Too many missing → go left
            right = mid - 1
    
    # After binary search, `left` is number of elements <= answer
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
