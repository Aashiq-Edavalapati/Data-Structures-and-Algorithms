from typing import List

def maxNonAdjSum(ind: int, arr: List[int], n:int, dp: List[int]) -> int:
    if ind >= n:    # Base Case
        return 0
    if dp[ind] != -1: return dp[ind]

    # Pick the current element => Skip the next element
    pick = maxNonAdjSum(ind + 2, arr, n, dp) + arr[ind]

    # Not picking the current element => Try the next element
    notPick = maxNonAdjSum(ind + 1, arr, n, dp)
    
    # Return the maximum of both
    dp[ind] = max(pick, notPick)
    return dp[ind]

if __name__ == '__main__':
    testCases = [
        [1,2,3,1],
        [2,7,9,3,1]
    ]
    for i, arr in enumerate(testCases):
        dp = [-1] * len(arr)
        print(f'TestCase {i}: i/p: {arr} o/p: {maxNonAdjSum(0, arr, len(arr), dp)}')