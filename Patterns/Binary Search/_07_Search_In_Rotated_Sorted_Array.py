from typing import List

# -----------------------------------------------------------------------------
# Problem: Search in Rotated Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   Given a rotated sorted array `arr` and an integer `target`, find the index
#   of `target` if it exists, otherwise return -1.
#
#   The array was originally sorted in ascending order but then rotated
#   at some pivot unknown to you.
#
# -----------------------------------------------------------------------------
# @pattern: Modified Binary Search
# -----------------------------------------------------------------------------
#
# @method:
#   1. Perform binary search as usual, but determine which half of the array
#      is sorted at each step.
#   2. If the target lies within the sorted half, discard the other half.
#   3. Repeat until target is found or search space is exhausted.
#
# -----------------------------------------------------------------------------
# Intuition:
#   A rotated sorted array still contains two sorted halves. By checking which
#   half is sorted at each step, we can decide where to search next, ensuring
#   O(log n) time complexity.
# -----------------------------------------------------------------------------

def bruteForceSearch(arr: List[int], target: int) -> int:
    """
    Brute force search to find the index of `target` in the array.

    Parameters:
        arr (List[int]): The rotated sorted array.
        target (int): Value to search for.

    Returns:
        int: Index of target if found, otherwise -1.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


def searchInRotatedSortedArray(arr: List[int], target: int) -> int:
    """
    Searches for `target` in a rotated sorted array using modified binary search.

    Parameters:
        arr (List[int]): Rotated sorted array.
        target (int): Value to search for.

    Returns:
        int: Index of target if found, otherwise -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Found the target
        if arr[mid] == target:
            return mid

        # Check which half is sorted
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Search left half
            else:
                left = mid + 1   # Search right half
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Search right half
            else:
                right = mid - 1  # Search left half

    return -1


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing Search in Rotated Sorted Array ---")
    test_cases = [
        ([8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        ([1], 1)
    ]

    for i, (arr, target) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {target}")

        brute_result = bruteForceSearch(arr, target)
        binary_result = searchInRotatedSortedArray(arr, target)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")

        if brute_result == binary_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")
