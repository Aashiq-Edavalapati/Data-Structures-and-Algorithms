from typing import List, Tuple

# -----------------------------------------------------------------------------
# Problem: Minimum Days to Make m Bouquets
# -----------------------------------------------------------------------------
#
# @question:
#   You are given an integer array `boquets` where boquets[i] is the day the
#   ith flower will bloom. You are also given integers m and k.
#
#   You must make `m` bouquets, each containing exactly `k` flowers.
#   The flowers for each bouquet must be adjacent in the garden.
#
#   Return the minimum number of days needed to make `m` bouquets.
#   If it is not possible, return -1.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Answer
# -----------------------------------------------------------------------------
#
# @method:
#   1. The earliest possible day is min(boquets), latest is max(boquets).
#   2. Binary search on days:
#       - Use a helper function `isPossible` to check if we can make
#         at least m bouquets in `mid` days.
#       - If possible, try smaller days (move right pointer left).
#       - If not possible, try more days (move left pointer right).
# -----------------------------------------------------------------------------

def bruteForceMinDays(boquets: List[int], m: int, k: int) -> int:
    """
    Brute force method: Check each day from min to max until possible.

    Time Complexity: O(Range * N)  # range = max - min + 1
    Space Complexity: O(1)
    """
    if m * k > len(boquets):
        return -1

    for days in range(min(boquets), max(boquets) + 1):
        if isPossible(boquets, days, m, k):
            return days
    return -1


def isPossible(boquets: List[int], days: int, m: int, k: int) -> bool:
    """
    Checks if we can make at least m bouquets in 'days'.

    Args:
        boquets (List[int]): Days when each flower blooms.
        days (int): The maximum allowed bloom day.
        m (int): Required bouquets.
        k (int): Flowers per bouquet.

    Returns:
        bool: True if possible, False otherwise.
    """
    if m * k > len(boquets):
        return False

    count, noOfBo = 0, 0
    for bloom in boquets:
        if bloom <= days:
            count += 1
        else:
            noOfBo += count // k
            count = 0
        if noOfBo >= m:
            return True

    noOfBo += count // k
    return noOfBo >= m


def minDays(boquets: List[int], m: int, k: int) -> int:
    """
    Finds minimum days to make m bouquets.

    Time Complexity: O(N log Range)
    Space Complexity: O(1)
    """
    if m * k > len(boquets):
        return -1

    left, right = min(boquets), max(boquets)
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2
        if isPossible(boquets, mid, m, k):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing Minimum Days to Make m Bouquets ---")
    test_cases: Tuple[Tuple[List[int], int, int], int] = [
        (([7, 7, 7, 7, 13, 11, 12, 7], 2, 3), 12),
        (([1, 10, 3, 10, 2], 3, 1), 3),
        (([1, 10, 3, 10, 2], 3, 2), -1),  # impossible
        (([1, 2, 3, 4, 5], 2, 3), -1)    # impossible
    ]

    for i, ((boquets, m, k), expected) in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i} ---")
        print(f"Input boquets = {boquets}, m = {m}, k = {k}")
        brute_result = bruteForceMinDays(boquets, m, k)
        binary_result = minDays(boquets, m, k)
        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")
        print(f"Expected Result: {expected}")
        if brute_result == binary_result == expected:
            print("✅ Both match expected output")
        else:
            print("❌ Mismatch detected")
