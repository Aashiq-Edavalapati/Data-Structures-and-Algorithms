# -----------------------------------------------------------------------------
# Problem: Upper Bound in Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   Find the index `ind` of the smallest element in a sorted array such that
#   arr[ind] > x. If no such element exists, return -1.
#
# @pattern:
#   Sorted array + boundary query (“first index where arr[i] > x”). 
#   Define a monotonic predicate P(i): arr[i] > x → False … False, True … True. 
#   Since the predicate flips once and stays True, binary search the index space for the first True (upper bound).
#
# -----------------------------------------------------------------------------


def brute_force_upper_bound(arr, x):
    """
        Brute Force Approach:
        Iterate through the array from the beginning and find the first index
        where arr[i] > x.

        Time Complexity: O(N) — must check each element in the worst case.
        Space Complexity: O(1)

        Parameters:
            arr (list[int]): Sorted list of integers.
            x (int): The target value.

        Returns:
            int: Index of the first element > x, or -1 if none exists.
    """
    for i in range(len(arr)):
        if arr[i] > x:
            return i
    return -1


def upper_bound(arr, x):
    """
        Optimized Approach: Binary Search

        Finds the index of the smallest element in a sorted array such that
        arr[ind] > x.

        Time Complexity: O(log N) — halves the search space each iteration.
        Space Complexity: O(1)

        Parameters:
            arr (list[int]): Sorted list of integers.
            x (int): The target value.

        Returns:
            int: Index of the first element > x, or -1 if none exists.
    """
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow in other languages

        if arr[mid] <= x:
            # Target must be to the right of mid
            left = mid + 1
        else:
            # arr[mid] > x — mid is a potential answer
            ans = mid
            right = mid - 1  # Try to find an even smaller index

    return ans


# -----------------------------------------------------------------------------
# Driver Code for Testing
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Testing Upper Bound Implementations ---")

    test_cases = [
        ([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 11),  # Expected index = 9 (arr[9] = 12)
        ([1, 2, 3, 4, 5], 3),                      # Expected index = 3
        ([1, 2, 3, 4, 5], 5),                      # Expected index = -1
        ([5, 6, 7], 5),                            # Expected index = 1
        ([5, 6, 7], 4),                            # Expected index = 0
        ([5, 6, 7], 8)                             # Expected index = -1
    ]

    for i, (arr, x) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Array: {arr}")
        print(f"Target: {x}")

        brute_result = brute_force_upper_bound(arr, x)
        binary_result = upper_bound(arr, x)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")

        if brute_result == binary_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")