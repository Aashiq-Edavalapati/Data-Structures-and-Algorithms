from typing import List

def minEnergy(ind: int, heights: List[int], dp: List[int]) -> int:
    if ind == 0: return 0
    if ind == 1: return heights[1]
    if dp[ind] != -1: return dp[ind]

    oneJump = minEnergy(ind - 1, heights, dp) + abs(heights[ind] - heights[ind - 1])
    twoJumps = minEnergy(ind - 2, heights, dp) + abs(heights[ind] - heights[ind - 2])
    dp[ind] = min(oneJump, twoJumps)

    return dp[ind]

if __name__ == '__main__':
    testCases = [
        [30, 10, 60, 10, 60, 50]
    ]
    for i, heights in enumerate(testCases):
        n = len(heights)
        dp = [-1] * n
        print(f'TestCase {i}: i/p: {heights} o/p: {minEnergy(len(heights) - 1, heights, dp)}')