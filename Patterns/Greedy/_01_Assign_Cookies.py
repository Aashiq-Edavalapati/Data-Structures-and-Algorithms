# -----------------------------------------------------------------------------
# Problem: Assign Cookies
# -----------------------------------------------------------------------------
#
# @question:
# You are given two integer arrays:
# - `greed[i]`: the minimum size of a cookie each child needs.
# - `cookies[j]`: the size of each cookie.
# A child will be content if greed\[i] ≤ cookie\[j].
# Each child can receive at most one cookie, and each cookie can be given to
# at most one child.
#
# Find the maximum number of content children.
#
# -----------------------------------------------------------------------------
# @pattern: Greedy (Sort + Two Pointers)
# - Each child has a minimum demand (greed).
# - Each cookie has a certain size (supply).
# - To maximize content children:
# → Always try to satisfy the "least greedy" child first
# with the smallest possible cookie.
#
# Why Greedy Works:
# * Greedy-choice property:
# Giving the smallest sufficient cookie to the least greedy child
# never blocks a better option later.
# * Optimal substructure:
# After satisfying one child optimally, the rest reduces to the same
# smaller problem.
#
# Greedy Pattern:
# - "Sort + Matching" → Sort both greed and cookies.
# - Walk with two pointers, greedily assign cookies whenever possible.
#
# -----------------------------------------------------------------------------
# @method (easy steps):
# 1. Sort greed\[] and cookies\[].
# 2. Use two pointers i, j for children and cookies.
# 3. If cookie\[j] satisfies greed\[i], assign it → move both pointers.
# 4. Else, move cookie pointer only (try bigger cookie).
# 5. Count how many children got cookies.
#
# Time Complexity: O(N log N + M log M)
# Space Complexity: O(1)

# ==============================================================================

def assignCookies(greed, cookies):
    greed.sort()
    cookies.sort()

    i, j = 0, 0
    n, m = len(greed), len(cookies)
    while i < n and j < m:
        if greed[i] <= cookies[j]:
            i += 1   # child is satisfied
        j += 1       # move to next cookie

    return i


# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    testCases = [
        # 1 child per cookie match
        ([1, 5, 3, 3, 4], [4, 2, 1, 2, 1, 3]),   # Expected: 4
        # Exact matches
        ([1, 2, 3], [1, 1]),                     # Expected: 1
        # More cookies than children
        ([1, 2], [1, 2, 3]),                     # Expected: 2
        # No cookie can satisfy any child
        ([5, 6, 7], [1, 2, 3]),                  # Expected: 0
        # Equal greed and cookie sizes
        ([2, 2, 2], [2, 2]),                     # Expected: 2
        # Large cookie satisfies multiple possible, but only once
        ([1, 2, 3], [3]),                        # Expected: 1
    ]


    i = 0
    for greed, cookies in testCases:
        print(f'TestCase {i}: {assignCookies(greed, cookies)}')
        i += 1