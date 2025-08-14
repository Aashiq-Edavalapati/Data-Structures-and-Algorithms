# -----------------------------------------------------------------------------
# Problem: Search Insert Position
# -----------------------------------------------------------------------------
#
# @question:
#   Given a sorted array `arr` and a target value `m`, return the index if the
#   target is found. If not, return the index where it would be inserted in
#   order. The array contains distinct values.
#
# @pattern:
#   Find Boundary in Monotonic Condition (Standard Binary Search Pattern)
#
# @method:
#   Binary Search to Find Exact Position or Insertion Index
#
# -----------------------------------------------------------------------------


from typing import List


def brute_force_search_insert(arr: List[int], m: int) -> int:
    """
        Brute Force Approach:
        Scan the array from left to right:
        - If the target is found, return its index.
        - If we find an element greater than the target, return that index.
        - If the target is greater than all elements, return len(arr).

        Time Complexity: O(N)
        Space Complexity: O(1)

        Parameters:
            arr (List[int]): Sorted list of distinct integers.
            m (int): Target value to search for.

        Returns:
            int: Index of the target or insertion position.
    """
    for i in range(len(arr)):
        if arr[i] >= m:
            return i
    return len(arr)


def search_insert_position(arr: List[int], m: int) -> int:
    """
        Optimized Approach: Binary Search

        Uses binary search to find:
        - The index of the target if it exists.
        - The index where the target should be inserted if it does not exist.

        Time Complexity: O(log N)
        Space Complexity: O(1)

        Parameters:
            arr (List[int]): Sorted list of distinct integers.
            m (int): Target value to search for.

        Returns:
            int: Index of the target or insertion position.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == m:
            return mid
        elif arr[mid] < m:
            left = mid + 1
        else:
            right = mid - 1

    # If not found, `left` will be the correct insertion index
    return left


# -----------------------------------------------------------------------------
# Driver Code for Testing
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Testing Search Insert Position Implementations ---")

    test_cases = [
        ([1, 3, 5, 6], 5),    # Expected = 2
        ([1, 3, 5, 6], 2),    # Expected = 1
        ([1, 3, 5, 6], 7),    # Expected = 4
        ([1, 3, 5, 6], 0),    # Expected = 0
        ([], 0)               # Expected = 0
    ]

    for i, (arr, m) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {m}")

        brute_result = brute_force_search_insert(arr, m)
        binary_result = search_insert_position(arr, m)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")

        if brute_result == binary_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")
