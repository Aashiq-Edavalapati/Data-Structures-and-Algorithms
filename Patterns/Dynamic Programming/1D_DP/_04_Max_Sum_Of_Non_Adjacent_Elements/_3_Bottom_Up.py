from typing import List

def maxNonAdjSum(arr: List[int]) -> int:
    n = len(arr) 
    dp = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 2] + arr[i], dp[i + 1])

    return dp[0]

if __name__ == '__main__':
    testCases = [
        [1,2,3,1],
        [2,7,9,3,1]
    ]
    for i, arr in enumerate(testCases):
        print(f'TestCase {i}: i/p: {arr} o/p: {maxNonAdjSum(arr)}')