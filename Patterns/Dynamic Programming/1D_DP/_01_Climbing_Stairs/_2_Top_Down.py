from typing import List

def countWaysToClimb(n: int, dp: List[int]) -> int:
    if n == 0: return 1
    if n == 1: return 1
    if dp[n] != -1: return dp[n]

    dp[n] = countWaysToClimb(n - 1, dp) + countWaysToClimb(n - 2, dp)

    return dp[n]

if __name__ == '__main__':
    testCases = list(range(46))
    for i, n in enumerate(testCases):
        dp = [-1] * (n + 1)
        print(f'TestCase {i}: i/p: {n} o/p:{countWaysToClimb(n, dp)}')