from typing import List

# -----------------------------------------------------------------------------
# Problem: Search in Rotated Sorted Array with Duplicates
# -----------------------------------------------------------------------------
#
# @question:
#   Given a rotated sorted array `arr` (which may contain duplicates) and an
#   integer `target`, find the index of `target` if it exists, otherwise
#   return -1.
#
#   The array was originally sorted in ascending order but then rotated at
#   some pivot unknown to you.
#
# -----------------------------------------------------------------------------
# @pattern: Modified Binary Search
# -----------------------------------------------------------------------------
#
# @method:
#   1. Perform binary search, but handle duplicates by shrinking the search
#      range when `arr[left] == arr[mid] == arr[right]`.
#   2. At each step, determine which half is sorted and check if the target
#      lies within it.
#   3. Discard the irrelevant half and continue searching until found or
#      search space is empty.
#
# -----------------------------------------------------------------------------
# Intuition:
#   When duplicates are present, standard "rotated sorted" logic might fail
#   because the equality condition can hide the sorted half. By incrementing
#   `left` and decrementing `right` when `arr[left] == arr[mid] == arr[right]`,
#   we effectively skip over duplicates without losing the target.
# -----------------------------------------------------------------------------

def bruteForceSearch(arr: List[int], target: int) -> int:
    """
        Brute force search to find the index of `target` in the array.

        Parameters:
            arr (List[int]): Rotated sorted array (may contain duplicates).
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


def searchInRotatedSortedArrayWithDuplicates(arr: List[int], target: int) -> int:
    """
        Searches for `target` in a rotated sorted array that may contain duplicates.

        Parameters:
            arr (List[int]): Rotated sorted array (may contain duplicates).
            target (int): Value to search for.

        Returns:
            int: Index of target if found, otherwise -1.

        Time Complexity: O(log n) in best/average case, O(n) in worst case (all duplicates).
        Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Found the target
        if arr[mid] == target:
            return mid

        # Handle duplicates: can't determine sorted half
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
            continue

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
    print("--- Testing Search in Rotated Sorted Array with Duplicates ---")
    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0),    # target in rotated right half
        ([2, 5, 6, 0, 0, 1, 2], 3),    # target not present
        ([1, 1, 1, 1, 1], 1),          # all duplicates, target present
        ([1, 1, 1, 1, 1], 2),          # all duplicates, target absent
        ([1, 3, 1, 1, 1], 3)           # tricky duplicate rotation
    ]

    for i, (arr, target) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {target}")

        brute_result = bruteForceSearch(arr, target)
        binary_result = searchInRotatedSortedArrayWithDuplicates(arr, target)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")

        if brute_result == binary_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")
