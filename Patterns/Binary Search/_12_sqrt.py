# -----------------------------------------------------------------------------
# Problem: Integer Square Root using Binary Search
# -----------------------------------------------------------------------------
#
# @question:
#   Given a non-negative integer `n`, return the integer part of its square root.
#   In other words, return ⌊sqrt(n)⌋.
#
# -----------------------------------------------------------------------------
# @pattern: 
#   We’re looking for the largest integer whose square ≤ n. 
#   The predicate mid*mid ≤ n is monotonic (once it becomes false, it stays false for larger mids). 
#   This makes it a classic Binary Search on Answer problem.
# -----------------------------------------------------------------------------
#
# @method:
#   1. Search between 1 and n for the largest integer whose square is <= n.
#   2. If mid*mid <= n, store mid as a possible answer and move right to find larger.
#   3. If mid*mid > n, move left to find smaller possible values.
#
# -----------------------------------------------------------------------------
# Intuition:
#   Instead of incrementing by 1 (O(√n)), we use binary search to cut the search
#   range in half each step, achieving O(log n) time complexity.
# -----------------------------------------------------------------------------

def bruteForceSqrt(n: int) -> int:
    """
    Brute force approach to find integer square root.

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Floor of square root of n.
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    if n < 0:
        return -1
    i = 0
    while i * i <= n:
        i += 1
    return i - 1


def sqrt(n: int) -> int:
    """
    Finds floor(sqrt(n)) using binary search on the answer.

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Floor of sqrt(n), or -1 if n < 0.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if n < 0:
        return -1
    if n < 2:
        return n

    left, right = 1, n
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


def sqrtExactOrFloor(n: int) -> int:
    """
    Finds sqrt(n) if exact, else returns floor(sqrt(n)).

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Exact sqrt(n) if perfect square, else floor(sqrt(n)).

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if n < 0:
        return -1
    if n < 2:
        return n

    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        product = mid * mid

        if product == n:
            return mid
        elif product < n:
            left = mid + 1
        else:
            right = mid - 1

    return right


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing Integer Square Root ---")
    test_cases = [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (16, 4),
        (26, 5),
        (100, 10),
        (99, 9)
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"n = {n}")

        brute_result = bruteForceSqrt(n)
        binary_result = sqrt(n)
        exact_or_floor_result = sqrtExactOrFloor(n)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Floor Result: {binary_result}")
        print(f"Exact-or-Floor Result: {exact_or_floor_result}")
        print(f"Expected Floor: {expected}")

        if brute_result == binary_result == exact_or_floor_result == expected:
            print("✅ Results match expected output!")
        else:
            print("❌ Mismatch detected!")
