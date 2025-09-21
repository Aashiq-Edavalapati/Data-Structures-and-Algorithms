from typing import List
# if n == 0: return 1
# if n == 1: return 1
# return countWaysToClimb(n - 1) + countWaysToClimb(n - 2)

def minEnergy(heights: List[int]) -> int:
    n = len(heights)
    dp = [0] * n
    dp[0] = 0 # Base Case
    dp[1] = heights[1] # Base Case
    for i in range(2, n):
        # Replace f(n) with dp[n] in the recurrence relation
        dp[i] = min((dp[i - 1] + abs(heights[i] - heights[i - 1])), (dp[i - 2] + abs(heights[i] - heights[i - 2])))

    return dp[n - 1] # Required answer f(n - 1) => dp[n - 1]

if __name__ == '__main__':
    testCases = [
        [30, 10, 60, 10, 60, 50]
    ]
    for i, heights in enumerate(testCases):
        print(f'TestCase {i}: i/p: {heights} o/p: {minEnergy(heights)}')