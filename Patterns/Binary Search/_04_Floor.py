from typing import List

# -----------------------------------------------------------------------------
# Problem: Floor of an Element in Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   Given a sorted array `arr` and an integer `x`, find the index of the
#   floor of `x` in the array.
#   The floor of `x` is defined as the greatest element in the array
#   that is less than or equal to `x`.
#
# -----------------------------------------------------------------------------
#
# @pattern: 
#   Sorted array + boundary query (“greatest element ≤ x”). 
#   Define monotonic predicate P(i): arr[i] ≤ x → True … True, False … False. 
#   Since it flips once and stays False, you can binary search for the last True (floor).
#
# =============================================================================


def bruteForce_floor(arr: List[int], x: int) -> int:
    """
        Brute force approach to find the floor index of x.

        This function iterates through the array linearly and keeps track of
        the index of the largest element <= x.

        Time Complexity: O(N)
        Space Complexity: O(1)

        Parameters:
            - arr (List[int]): A sorted list of integers.
            - x (int): The target value.

        Returns:
            - int: The index of the floor of x. Returns -1 if floor doesn't exist.
    """
    ans = -1
    for i in range(len(arr)):
        if arr[i] <= x:
            ans = i
        else:
            break
    return ans


def floor(arr: List[int], x: int) -> int:
    """
        Optimized approach using Binary Search to find the floor index of x.

        The function searches for the greatest element <= x in a sorted array
        by adjusting search bounds until the largest possible valid index is found.

        Time Complexity: O(log N)
        Space Complexity: O(1)

        Parameters:
            - arr (List[int]): A sorted list of integers.
            - x (int): The target value.

        Returns:
            - int: The index of the floor of x. Returns -1 if floor doesn't exist.
    """
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2  # Middle index

        if arr[mid] > x:
            # Floor must be in left half
            right = mid - 1
        else:
            # arr[mid] <= x → valid floor candidate
            ans = mid
            left = mid + 1  # Search right half for a possibly larger floor

    return ans


if __name__ == '__main__':
    print("--- Testing Floor Solutions ---")

    # Test cases: (array, target)
    test_cases = [
        ([10, 20, 22, 30, 40, 50], 25),
        ([1, 2, 8, 10, 10, 12, 19], 5),
        ([1, 2, 8, 10, 10, 12, 19], 20),
        ([5, 6, 7], 4),  # No floor exists
    ]

    for i, (arr, x) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {x}")

        brute_result = bruteForce_floor(arr, x)
        binary_result = floor(arr, x)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")

        if brute_result == binary_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")
