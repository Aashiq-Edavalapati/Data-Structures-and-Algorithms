# -----------------------------------------------------------------------------
# Problem: Nth Root of an Integer
# -----------------------------------------------------------------------------
#
# @question:
#   Given two integers n and m, find an integer x such that x^n = m.
#   If no such integer exists, return -1.
#
# -----------------------------------------------------------------------------
# @pattern: 
#   We’re searching for an integer x such that x^n = m. 
#   The function f(x) = x^n is monotonic increasing for positive integers. 
#   That means if mid^n < m, larger values may work; if mid^n > m, smaller values may work. 
#   This monotonic property lets us binary search on the answer in the range [1, m].
# -----------------------------------------------------------------------------
#
# @method:
#   1. Search between 1 and m (inclusive) for x.
#   2. Use a helper function to compare x^n with m without overflow:
#       - Return 1 if equal
#       - Return 0 if less
#       - Return 2 if greater
#   3. Adjust search space accordingly.
#
# -----------------------------------------------------------------------------
# Intuition:
#   Instead of testing all numbers from 1 to m, we can halve the search space
#   each step using binary search.
# -----------------------------------------------------------------------------

from typing import Tuple

def bruteForceNthRoot(n: int, m: int) -> int:
    """
    Brute force approach to find nth root of m.

    Time Complexity: O(m)
    Space Complexity: O(1)
    """
    if m < 0 or n <= 0:
        return -1

    for x in range(1, m + 1):
        power = 1
        for _ in range(n):
            power *= x
        if power == m:
            return x
        if power > m:
            break
    return -1


def helper(mid: int, n: int, m: int) -> int:
    """
    Helper function to compare mid^n with m without unnecessary computation.

    Returns:
        1 if mid^n == m
        0 if mid^n < m
        2 if mid^n > m
    """
    ans = 1
    for _ in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0


def nthRoot(n: int, m: int) -> int:
    """
    Finds integer nth root of m using binary search.

    Parameters:
        n (int): The degree of the root.
        m (int): The number to find the root of.

    Returns:
        int: The integer x such that x^n = m, or -1 if no such integer exists.

    Time Complexity: O(log m * n)  # binary search * exponentiation steps
    Space Complexity: O(1)
    """
    if m < 0 or n <= 0:
        return -1
    if m in (0, 1):
        return m

    left, right = 1, m
    while left <= right:
        mid = left + (right - left) // 2

        condition = helper(mid, n, m)
        if condition == 1:
            return mid
        elif condition == 0:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing Nth Root ---")
    test_cases: Tuple[Tuple[int, int], int] = [
        ((2, 16), 4),    # perfect square
        ((3, 27), 3),    # perfect cube
        ((4, 81), 3),    # perfect 4th root
        ((3, 15), -1),   # not a perfect cube
        ((5, 243), 3),   # perfect 5th root
        ((2, 1), 1),     # edge case m=1
        ((2, 0), 0)      # edge case m=0
    ]

    for i, ((n, m), expected) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"n = {n}, m = {m}")

        brute_result = bruteForceNthRoot(n, m)
        binary_result = nthRoot(n, m)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")
        print(f"Expected Result: {expected}")

        if brute_result == binary_result == expected:
            print("✅ Both methods match expected output!")
        else:
            print("❌ Mismatch detected!")
