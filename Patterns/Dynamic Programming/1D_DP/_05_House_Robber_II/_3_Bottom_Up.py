from typing import List

def maxNonAdjSum(arr: List[int]) -> int:
    n = len(arr) 
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])

    return dp[n - 1]

def houseRobber2(arr: List[int]) -> int:
    arr1 = arr[1:]
    arr2 = arr[:-1]
    return max(maxNonAdjSum(arr1), maxNonAdjSum(arr2))

if __name__ == '__main__':
    testCases = [
        [2, 3, 2], # 3
        [1, 2, 3], # 3
        [1, 2, 3, 1], # 4
        [2, 7, 9, 3, 1] # 11
    ]
    for i, arr in enumerate(testCases):
        print(f'TestCase {i}: i/p: {arr} o/p: {houseRobber2(arr)}')