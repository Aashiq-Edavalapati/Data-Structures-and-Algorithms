# -----------------------------------------------------------------------------
# Problem: Lower Bound in Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   Find the index `ind` of the smallest element in a sorted array such that
#   `arr[ind] >= x`. If no such element exists, return -1.
#
# @pattern:
#   Find Boundary in Monotonic Condition (Standard Binary Search Pattern)
#
# @method:
#   Binary Search for First Element >= Target
#
# -----------------------------------------------------------------------------


def brute_force_lower_bound(arr, x):
    """
        Brute Force Approach:
        Iterate through the array from the beginning and find the first index
        where arr[i] >= x.

        Time Complexity: O(N) — must check each element in the worst case.
        Space Complexity: O(1)

        Parameters:
            arr (list[int]): Sorted list of integers.
            x (int): The target value.

        Returns:
            int: Index of the first element >= x, or -1 if none exists.
    """
    for i in range(len(arr)):
        if arr[i] >= x:
            return i
    return -1


def lower_bound(arr, x):
    """
        Optimized Approach: Binary Search

        Finds the index of the smallest element in a sorted array such that
        arr[ind] >= x.

        Time Complexity: O(log N) — halves the search space each iteration.
        Space Complexity: O(1)

        Parameters:
            arr (list[int]): Sorted list of integers.
            x (int): The target value.

        Returns:
            int: Index of the first element >= x, or -1 if none exists.
    """
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids potential overflow in other languages

        if arr[mid] < x:
            # Target must be in the right half
            left = mid + 1
        else:
            # arr[mid] >= x — mid is a potential answer
            ans = mid
            right = mid - 1  # Try to find a smaller index

    return ans


# -----------------------------------------------------------------------------
# Driver Code for Testing
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Testing Lower Bound Implementations ---")

    test_cases = [
        ([3, 5, 8, 15, 19], 9),    # Expected index = 3 (arr[3] = 15)
        ([1, 2, 3, 4, 5], 3),      # Expected index = 2
        ([1, 2, 3, 4, 5], 6),      # Expected index = -1 (no element >= 6)
        ([5, 6, 7], 5),            # Expected index = 0
        ([5, 6, 7], 4),            # Expected index = 0
        ([5, 6, 7], 8)             # Expected index = -1
    ]

    for i, (arr, x) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {x}")

        brute_result = brute_force_lower_bound(arr, x)
        binary_result = lower_bound(arr, x)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")

        if brute_result == binary_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")
