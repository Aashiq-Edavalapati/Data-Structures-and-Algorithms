from typing import List

# -----------------------------------------------------------------------------
# Problem: Capacity to Ship Packages Within D Days
# -----------------------------------------------------------------------------
#
# @question:
#   You are given an array `weights` representing the weights of packages
#   and an integer `days` representing the number of days to deliver them.
#   Packages must be shipped in order and the total weight on each day
#   cannot exceed the ship's capacity.
#
#   Find the minimum ship capacity needed to ship all packages within `days`.
#
# -----------------------------------------------------------------------------
#
# @pattern: Binary Search on Answer
#
# -----------------------------------------------------------------------------
#
# @method:
#   1. The minimum possible capacity is `max(weights)` (must fit heaviest package).
#   2. The maximum possible capacity is `sum(weights)` (ship all in one day).
#   3. Binary search over this capacity range:
#       - Check if it's possible to ship within `days` given a trial capacity.
#       - If possible, try smaller capacity (move left).
#       - If not possible, increase capacity (move right).
#
# Time Complexity: O(N log(sum(weights) - max(weights)))
# Space Complexity: O(1)
# ==============================================================================

def isPossible(weights: List[int], capacity: int, days: int) -> bool:
    """
    Checks if it is possible to ship all packages within `days`
    using a ship with given `capacity`.
    """
    curr_days = 1
    curr_weight = 0
    for weight in weights:
        curr_weight += weight
        if curr_weight > capacity:
            curr_weight = weight
            curr_days += 1
            if curr_days > days:
                return False
    return True

def minCapacity(weights: List[int], days: int) -> int:
    """
    Finds the minimum capacity required to ship all packages within `days`.
    """
    left, right = max(weights), sum(weights)

    while left <= right:
        mid = left + (right - left) // 2
        if isPossible(weights, mid, days):
            right = mid - 1  # Try smaller capacity
        else:
            left = mid + 1  # Increase capacity
    return left

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([3, 2, 2, 4, 1, 4], 3),
        ([1, 2, 3, 1, 1], 4)
    ]
    for i, (weights, days) in enumerate(test_cases, start=1):
        print(f"Test Case {i}: Minimum Capacity = {minCapacity(weights, days)}")
