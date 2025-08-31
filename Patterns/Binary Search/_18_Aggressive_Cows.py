# -----------------------------------------------------------------------------
# Problem: Aggressive Cows
# -----------------------------------------------------------------------------
#
# @question:
#   We are given the positions of stalls (arr) and the number of cows (cows).
#   We want to place all cows in the stalls so that the minimum distance
#   between any two cows is as large as possible.
#
#   Return the largest minimum distance possible.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Answer
#   - We are not searching inside the array directly.
#   - We search for the maximum distance (answer) that still allows placing all cows.
#   - Monotonic property:
#       If a distance `d` is possible, then all distances smaller than `d` are possible too.
#       If a distance `d` is not possible, then all distances larger than `d` are also impossible.
#   - This monotonicity → Binary Search on Answer.
#
# -----------------------------------------------------------------------------
# @method (easy steps):
#   1. Sort stall positions.
#   2. Minimum possible distance = 1, maximum = last_stall - first_stall.
#   3. Binary search on this distance range:
#       - Check if we can place all cows with at least `mid` distance.
#       - If yes, try bigger distance (move left pointer up).
#       - If no, try smaller distance (move right pointer down).
#   4. The maximum valid distance will be stored in `right`.
#
# Time Complexity: O(N log(max_distance))
#   - For each distance checked, we try placing cows (O(N)).
#   - Distances are checked with binary search.
# Space Complexity: O(1)
# ==============================================================================

def canBePlaced(arr, cows, n, dist):
    """
    Check if cows can be placed in stalls with at least `dist` distance apart.
    """
    i = 1          # index for current stall being checked
    cows -= 1      # first cow is placed at arr[0]
    prev = 0       # index of last placed cow

    while i < n and cows > 0:
        # If current stall is too close to the last placed cow, skip it
        if arr[i] - arr[prev] < dist:
            i += 1
            continue

        # Place a cow here
        cows -= 1
        prev = i
        i += 1

    # Return True if all cows are placed successfully
    return cows == 0

def maxMinDist(arr, cows):
    """
    Find the maximum minimum distance possible for placing cows.
    """
    arr.sort()
    n = len(arr)

    left, right = 1, arr[-1] - arr[0]
    while left <= right:
        mid = left + (right - left) // 2

        if canBePlaced(arr, cows, n, mid):
            # If we can place cows with `mid` distance, try bigger distance
            left = mid + 1
        else:
            # Otherwise, try smaller distance
            right = mid - 1

    # At the end, `right` holds the maximum minimum distance possible
    return right

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    testCases = [
        ([0, 3, 4, 7, 9, 10], 4)
    ]

    i = 0
    for arr, cows in testCases:
        print(f'TestCase {i}: {maxMinDist(arr, cows)}')
        i += 1
