from typing import List

def minEnergy(ind: int, heights: List[int], k:int, dp: List[int]) -> int:
    if ind == 0: return 0
    if dp[ind] != -1: return dp[ind]

    minE = float('inf')
    for i in range(1, k + 1):
        if ind - i < 0: break
        minE = min(minE, minEnergy(ind - i, heights, k, dp) + abs(heights[ind] - heights[ind - i]))
    
    dp[ind] = minE
    return dp[ind]

if __name__ == '__main__':
    testCases = [
        ([10, 5, 20, 0, 15], 2),
        ([15, 4, 1, 14, 15], 3),
        ([15, 4, 1, 14, 15], 4)
    ]
    for i, inp in enumerate(testCases):
        heights, k = inp
        n = len(heights)
        dp = [-1] * n
        print(f'TestCase {i}: i/p: {heights} o/p: {minEnergy(len(heights) - 1, heights, k, dp)}')