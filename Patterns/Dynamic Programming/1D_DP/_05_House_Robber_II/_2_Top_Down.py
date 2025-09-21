from typing import List

def maxNonAdjSum(ind: int, arr: List[int], dp: List[int]) -> int:
    if ind < 0:    # Base Case
        return 0
    if ind == 0: return arr[0]
    if dp[ind] != -1: return dp[ind]

    # Pick the current element => Skip the next element
    pick = maxNonAdjSum(ind - 2, arr, dp) + arr[ind]

    # Not picking the current element => Try the next element
    notPick = maxNonAdjSum(ind - 1, arr, dp)
    
    # Return the maximum of both
    dp[ind] = max(pick, notPick)
    return dp[ind]

def houseRobber2(arr: List[int]) -> int:
    n = len(arr)
    arr1 = arr[1:]
    arr2 = arr[:-1]
    dp1 = [-1] * (n - 1)
    dp2 = dp1[:]
    return max(maxNonAdjSum(n - 2, arr1, dp1), maxNonAdjSum(n - 2, arr2, dp2))

if __name__ == '__main__':
    testCases = [
        [2,3,2], # 3
        [1, 2, 3], # 3
        [1,2,3,1], # 4
        [2,7,9,3,1] # 11
    ]
    for i, arr in enumerate(testCases):
        print(f'TestCase {i}: i/p: {arr} o/p: {houseRobber2(arr)}')