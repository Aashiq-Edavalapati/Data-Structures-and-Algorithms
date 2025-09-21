from typing import List
# if n == 0: return 1
# if n == 1: return 1
# return countWaysToClimb(n - 1) + countWaysToClimb(n - 2)

def minEnergy(heights: List[int], k: int) -> int:
    n = len(heights)
    dp = [0] * n
    for i in range(2, n):
        minE = float('inf')
        for j in range(1, k + 1):
            if j < 0:
                break
            minE = min(minE, dp[i - j] + abs(heights[i] - heights[i - j]))
        dp[i] = minE

    return dp[n - 1] # Required answer f(n - 1) => dp[n - 1]

if __name__ == '__main__':
    testCases = [
        ([10, 5, 20, 0, 15], 2),
        ([15, 4, 1, 14, 15], 3),
        ([15, 4, 1, 14, 15], 4)
    ]
    for i, inp in enumerate(testCases):
        heights, k = inp
        print(f'TestCase {i}: i/p: "heights"={heights}, k={k}\n{' '*12}o/p: {minEnergy(heights, k)}')
        print()