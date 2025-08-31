from typing import List

# -----------------------------------------------------------------------------
# Problem: Capacity to Ship Packages Within D Days
# -----------------------------------------------------------------------------
#
# @question:
#   You are given an array `weights` representing the weights of packages
#   and an integer `days` representing the number of days to deliver them.
#   Packages must be shipped in the given order, and the total weight each day
#   cannot exceed the ship's capacity.
#
#   Find the minimum ship capacity needed to ship all packages within `days`.
#
# -----------------------------------------------------------------------------
#
# @pattern: Binary Search on Answer
#   - We are not searching for an element in the array, but for the smallest
#     ship capacity that still works.
#   - Monotonicity: If a certain capacity can ship all packages in time, then
#     any bigger capacity will also work. This makes binary search possible.
#
# -----------------------------------------------------------------------------
#
# @method (simple steps):
#   1. The ship must carry at least the heaviest package. So min capacity is max(weights).
#   2. In the extreme case, ship everything in one day. So max capacity is sum(weights).
#   3. Binary search between [max(weights), sum(weights)]:
#       - Try mid capacity.
#       - If it's enough to ship within `days`, try smaller (move right pointer).
#       - If it's not enough, increase capacity (move left pointer).
#
# Time Complexity: O(N log(sum(weights) - max(weights)))
# Space Complexity: O(1)
# ==============================================================================

def isPossible(weights: List[int], capacity: int, days: int) -> bool:
    """
    Check if we can ship all packages in `days` with given ship `capacity`.

    We load packages in order. If adding a package exceeds the capacity,
    we move to the next day and reset the current weight.
    """
    curr_days = 1  # Start with day 1
    curr_weight = 0

    for weight in weights:
        curr_weight += weight
        if curr_weight > capacity:
            # If current package doesn't fit, start a new day
            curr_weight = weight
            curr_days += 1
            if curr_days > days:
                return False

    return True

def minCapacity(weights: List[int], days: int) -> int:
    """
    Find the minimum ship capacity needed to deliver all packages in `days`.
    """
    left, right = max(weights), sum(weights)

    while left <= right:
        mid = left + (right - left) // 2
        if isPossible(weights, mid, days):
            # If mid works, try to see if we can reduce capacity
            right = mid - 1
        else:
            # If mid is too small, increase capacity
            left = mid + 1
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
