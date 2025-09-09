# -----------------------------------------------------------------------------
# Problem: Jump Game
# -----------------------------------------------------------------------------
#
# @question:
# You are given an array arr where each element represents the maximum jump
# length from that position. Starting from index 0, return True if you can
# reach the last index, otherwise False.
#
# -----------------------------------------------------------------------------
# @pattern: Greedy (Range Carrying)
# - At each index, you can jump forward up to arr[i] steps.
# - Instead of trying all paths (DP/backtracking), greedily track the
#   farthest index you can reach at each step.
# - If at any point, your max reachable index is less than or equal to i
#   and arr[i] == 0, you're stuck → return False.
# - If your max reachable index ever reaches or passes the last index,
#   return True.
#
# Why Greedy Works:
# * Greedy-choice property:
#   Extending the farthest reach at each step never blocks future moves.
# * Optimal substructure:
#   Once you know the farthest reachable index up to i,
#   the rest of the problem is the same smaller subproblem.
#
# Greedy Pattern:
# - "Range-Carrying" → maintain [0, maxReach] window and keep extending.
#
# -----------------------------------------------------------------------------
# @method (easy steps):
# 1. Initialize maxReach = 0.
# 2. Iterate through array:
#    - Update maxReach = max(maxReach, i + arr[i]).
#    - If i > maxReach → stuck → return False.
#    - If maxReach >= last index → return True.
# 3. End loop → return True (reachable).
# Time Complexity: O(N)
# Space Complexity: O(1)

# ==============================================================================

def canReachEnd(arr):
    """
    Determines if the end of the array is reachable using a greedy approach.
    """
    maxReach = 0
    n = len(arr)

    for i in range(n):
        if i > maxReach:
            # We are at an index 'i' that is beyond our current
            # maximum reachable index. This means we're stuck.
            return False

        # Greedily extend the farthest reachable index.
        maxReach = max(maxReach, i + arr[i])

        if maxReach >= n - 1:
            # We have found a path that reaches or surpasses the last index.
            return True

    # This part of the code is technically unreachable due to the previous
    # check, but it's a valid safeguard. If the loop completes, it means
    # we've processed all indices without getting stuck.
    return True

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    testCases = [
        [2, 3, 1, 0, 4],  # True  → can jump 2 → 3 → end
        [3, 2, 1, 0, 4],  # False → stuck at 0
        [1, 2, 3, 1, 1, 0, 2, 5], # False → stuck at index 5
        [1, 2, 4, 1, 1, 0, 2, 5], # True  → jump 2 → 4 → end
        [0],  # True  → already at end
        [2, 0, 0], # True  → first jump reaches end
        [1, 0, 1, 0], # False → stuck at index 1
    ]

    i = 0
    for arr in testCases:
        print(f'TestCase {i}: {canReachEnd(arr)}')
        i += 1