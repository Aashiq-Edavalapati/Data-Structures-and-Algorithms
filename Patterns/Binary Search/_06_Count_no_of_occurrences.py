from typing import List
from _05_First_and_last_occurence import findFirstAndLastOccurrence

# -----------------------------------------------------------------------------
# Problem: Count the Number of Occurrences in a Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   Given a sorted array `arr` and a target value `x`, count the number of
#   times `x` appears in `arr`.
#
# @pattern:
#   Sorted array + duplicate handling. 
#   The task is to count occurrences, which boils down to finding the first and last boundary indices of x. 
#   Boundaries in a sorted search space follow a monotonic predicate (arr[mid] < x, arr[mid] > x), 
#   so two binary searches efficiently locate the range.
#
# -----------------------------------------------------------------------------
# Intuition:
#   To count occurrences of a number efficiently in a sorted array, we can
#   find:
#     1. The index of the first occurrence of `x`
#     2. The index of the last occurrence of `x`
#   The total count is simply: (last - first + 1)
#
#   This uses two binary searches — one to find each boundary — making the
#   solution O(log n).
#
# ==============================================================================

def countNoOfOccurrences(arr: List[int], x: int) -> int:
    """
    Counts the number of times `x` appears in a sorted list `arr`.

    Parameters:
        arr (List[int]): A sorted list of integers.
        x (int): The target value to count.

    Returns:
        int: The count of occurrences of `x` in `arr`.

    Time Complexity: O(log n) — relies on binary search for first and last occurrence.
    Space Complexity: O(1)
    """
    # Get the first and last occurrence indices using binary search
    first, last = findFirstAndLastOccurrence(arr, x)

    # If x does not exist in the array
    if first == -1:
        return 0

    # Count = last index - first index + 1
    return last - first + 1


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Testing Count No. of Occurrences ---")
    test_cases = [
        ([1, 2, 2, 2, 3, 4], 2),      # Multiple occurrences
        ([1, 1, 1, 1, 1], 1),         # All same elements
        ([1, 2, 3, 4, 5], 3),         # Single occurrence
        ([1, 2, 3, 4, 5], 6),         # Element not present
        ([], 0)                       # Empty array
    ]

    for i, (arr, target) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        result = countNoOfOccurrences(arr, target)
        print(f"Occurrences: {result}")
