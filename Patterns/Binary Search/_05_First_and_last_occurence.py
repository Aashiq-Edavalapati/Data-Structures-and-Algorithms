from typing import List
from _01_LowerBound import lowerBound
from _02_UpperBound import upperBound

# -----------------------------------------------------------------------------
# Problem: First and Last Occurrence of an Element in a Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   Given a sorted array `arr` and a target value `x`, find the indices of the
#   first and last occurrence of `x` in the array.
#
#   If `x` is not found, return (-1, -1).
#
# -----------------------------------------------------------------------------
#
# @pattern: Binary Search on Boundaries
#
# -----------------------------------------------------------------------------
#
# @method: Two-Pass Binary Search (One for First Occurrence, One for Last)
#
# =============================================================================


def firstOccurrence(arr: List[int], x: int) -> int:
    """
        Binary search to find the index of the first occurrence of x.

        Time Complexity: O(log N)
        Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            ans = mid
            right = mid - 1  # search left half for earlier occurrence
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans


def lastOccurrence(arr: List[int], x: int) -> int:
    """
        Binary search to find the index of the last occurrence of x.

        Time Complexity: O(log N)
        Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            ans = mid
            left = mid + 1  # search right half for later occurrence
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans


def findFirstAndLastOccurrence(arr: List[int], x: int) -> tuple:
    """
        Finds the first and last occurrence indices of x using two
        separate binary search functions.

        Returns:
            tuple: (first_index, last_index)
    """
    first = firstOccurrence(arr, x)
    if first == -1:
        return (-1, -1)

    last = lastOccurrence(arr, x)
    return (first, last)


# -----------------------------------------------------------------------------
# Alternative Optimized Method
# -----------------------------------------------------------------------------
#
# Uses lowerBound() and upperBound() helpers to find boundaries directly.
# Requires:
#   - lowerBound(arr, x) from _01_LowerBound
#   - upperBound(arr, x) from _02_UpperBound
# =============================================================================

def findFirstAndLastOccurrence2(arr: List[int], x: int) -> tuple:
    """
        Finds the first and last occurrence of x using lowerBound() and upperBound().

        Returns:
            tuple: (first_index, last_index)
    """
    lb = lowerBound(arr, x)
    if lb == len(arr) or arr[lb] != x:
        return (-1, -1)

    ub = upperBound(arr, x)
    return (lb, ub - 1)


# -----------------------------------------------------------------------------
# Brute Force Method
# -----------------------------------------------------------------------------
def bruteForce_findFirstAndLastOccurrence(arr: List[int], x: int) -> tuple:
    """
        Brute force linear scan to find the first and last occurrence.

        Time Complexity: O(N)
        Space Complexity: O(1)
    """
    first, last = -1, -1
    for i in range(len(arr)):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
    return (first, last)


# -----------------------------------------------------------------------------
# Driver Code
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing First and Last Occurrence Solutions ---")

    test_cases = [
        ([2, 4, 6, 8, 8, 8, 11, 13], 8),
        ([1, 2, 2, 2, 3, 4], 2),
        ([1, 1, 1, 1], 1),
        ([1, 2, 3, 4, 5], 6),
        ([], 5),
    ]

    for i, (arr, x) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {x}")

        brute_res = bruteForce_findFirstAndLastOccurrence(arr, x)
        bin_res = findFirstAndLastOccurrence(arr, x)
        helper_res = findFirstAndLastOccurrence2(arr, x)

        print(f"Brute Force: {brute_res}")
        print(f"Binary Search: {bin_res}")
        print(f"Helper-Based: {helper_res}")

        if brute_res == bin_res == helper_res:
            print("✅ All methods match!")
        else:
            print("❌ Mismatch detected!")
