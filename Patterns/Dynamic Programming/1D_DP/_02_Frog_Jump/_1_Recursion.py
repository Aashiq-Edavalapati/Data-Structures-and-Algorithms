from typing import List

"""
    3 steps:
        1. Represent everything in terms of indices.
            0, 1, ...., n => Treat each number as an index
        2. Do all possible stuffs acc. to the problem statement.
            Jump 1 step or Jump 2 steps => f(n - 1) and f(n - 2)
        3. Min => Min(all stuffs)
            Min(f(n - 1), f(n - 2))
"""

def minEnergy(ind: int, heights: List[int]) -> int:
    if ind == 0: return 0
    if ind == 1: return heights[1]

    oneJump = minEnergy(ind - 1, heights) + abs(heights[ind] - heights[ind - 1])
    twoJumps = minEnergy(ind - 2, heights) + abs(heights[ind] - heights[ind - 2])

    return min(oneJump, twoJumps)

if __name__ == '__main__':
    testCases = [
        [30, 10, 60, 10, 60, 50]
    ]
    for i, heights in enumerate(testCases):
        print(f'TestCase {i}: i/p: {heights} o/p: {minEnergy(len(heights) - 1, heights)}')