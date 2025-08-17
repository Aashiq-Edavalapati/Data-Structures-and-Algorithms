from typing import List

# -----------------------------------------------------------------------------
# Problem: Find Minimum Element in Rotated Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   Given a rotated sorted array `arr` (with no duplicates), find the minimum
#   element in the array.
#
# -----------------------------------------------------------------------------
# @pattern: Modified Binary Search
# -----------------------------------------------------------------------------
#
# @method:
#   1. Use binary search to determine which half is sorted at each step.
#   2. If the left half is sorted, the minimum could be `arr[left]`, and we
#      search the right half.
#   3. If the right half is sorted, the minimum could be `arr[mid]`, and we
#      search the left half.
#   4. Continue narrowing until the minimum is found.
#
# -----------------------------------------------------------------------------
# Intuition:
#   The smallest element is the "pivot" point where rotation happened.
#   By checking sorted halves, we can ignore large portions of the array,
#   ensuring O(log n) performance.
# -----------------------------------------------------------------------------

def bruteForceFindPivot(arr: List[int]) -> int:
    """
    Brute force approach to find the minimum element in a rotated sorted array.

    Parameters:
        arr (List[int]): Rotated sorted array (no duplicates).

    Returns:
        int: Minimum element in the array.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return None
    return min(arr)


def findPivotInRotatedSortedArray(arr: List[int]) -> int:
    """
    Finds the minimum element (pivot) in a rotated sorted array without duplicates.

    Parameters:
        arr (List[int]): Rotated sorted array (no duplicates).

    Returns:
        int: Minimum element in the array.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return None

    left, right = 0, len(arr) - 1
    pivot = arr[0]

    while left <= right:
        mid = left + (right - left) // 2

        # Left half is sorted
        if arr[left] <= arr[mid]:
            pivot = min(pivot, arr[left])  # Possible new min
            left = mid + 1                 # Search right half
        # Right half is sorted
        else:
            pivot = min(pivot, arr[mid])   # Possible new min
            right = mid - 1                # Search left half
        
    return pivot


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing Find Pivot in Rotated Sorted Array ---")
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([3, 4, 5, 1, 2], 1),
        ([1, 2, 3, 4, 5], 1),     # no rotation
        ([2, 3, 4, 5, 1], 1),
        ([10], 10)                # single element
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")

        brute_result = bruteForceFindPivot(arr)
        binary_result = findPivotInRotatedSortedArray(arr)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")
        print(f"Expected: {expected}")

        if brute_result == binary_result == expected:
            print("✅ Results match expected output!")
        else:
            print("❌ Mismatch detected!")
