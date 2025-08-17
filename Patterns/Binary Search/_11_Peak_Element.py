from typing import List

# -----------------------------------------------------------------------------
# Problem: Find Peak Element
# -----------------------------------------------------------------------------
#
# @question:
#   A peak element in an array is an element that is strictly greater than its
#   neighbors. Given an input array `arr`, find the index of any peak element.
#   The array may contain multiple peaks — return the index of any one of them.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search in Unsorted Array
# -----------------------------------------------------------------------------
#
# @method:
#   1. Check edge cases first — if the peak is at the start or end.
#   2. Use binary search in the middle:
#      - If arr[mid] is greater than both neighbors, it's a peak.
#      - If arr[mid] is part of an ascending slope, move right.
#      - Otherwise, move left.
# -----------------------------------------------------------------------------
# Intuition:
#   Even in an unsorted array, the properties of a "peak" guarantee that we can
#   discard half of the search space at each step.
# -----------------------------------------------------------------------------

def bruteForceFindPeak(arr: List[int]) -> int:
    """
    Brute force approach to find the index of a peak element.

    Parameters:
        arr (List[int]): The input array.

    Returns:
        int: Index of a peak element.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 1:
        return 0

    for i in range(n):
        left = arr[i - 1] if i - 1 >= 0 else float('-inf')
        right = arr[i + 1] if i + 1 < n else float('-inf')
        if arr[i] > left and arr[i] > right:
            return i
    return -1


def findPeak(arr: List[int]) -> int:
    """
    Finds the index of a peak element using binary search.

    Parameters:
        arr (List[int]): The input array.

    Returns:
        int: Index of a peak element, or -1 if not found.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    n = len(arr)

    # Edge cases: single element or peak at edges
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return n - 1

    left, right = 1, n - 2
    while left <= right:
        mid = left + (right - left) // 2

        # Peak found
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        # Move right if ascending slope
        elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
            left = mid + 1
        # Otherwise, move left
        else:
            right = mid - 1

    return -1


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing Find Peak Element ---")
    test_cases = [
        ([1, 2, 3, 1], 2),                # peak in middle
        ([1, 2, 1, 3, 5, 6, 4], 5),       # peak near end
        ([1], 0),                         # single element
        ([2, 1], 0),                      # peak at start
        ([1, 2], 1)                       # peak at end
    ]

    for i, (arr, expected_peak) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")

        brute_result = bruteForceFindPeak(arr)
        binary_result = findPeak(arr)

        print(f"Brute Force Peak Index: {brute_result}")
        print(f"Binary Search Peak Index: {binary_result}")

        if arr[brute_result] == arr[binary_result]:
            print("✅ Both methods found a valid peak!")
        else:
            print("❌ Mismatch in peak detection!")
