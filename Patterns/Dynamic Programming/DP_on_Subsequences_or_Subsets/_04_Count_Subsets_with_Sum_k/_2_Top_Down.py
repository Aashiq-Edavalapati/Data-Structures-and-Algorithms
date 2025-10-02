from typing import List
"""
    @question:
        Given an array arr of n integers and an integer K, count the number of subsets of the given array that have a sum equal to K. Return the result modulo (109 + 7).


        Examples:

            Input: arr = [2, 3, 5, 16, 8, 10], K = 10
            Output: 3
            Explanation: The subsets are [2, 8], [10], and [2, 3, 5].

        --------------------------------------------------------------

            Input: arr = [1, 2, 3, 4, 5], K = 5
            Output: 3
            Explanation: The subsets are [5], [2, 3], and [1, 4].
        
        Constraints:
            1 <= n <= 100
            1 <= arr[i] <= 103
            1 <= K <= 103
"""

def countSubsetsWithSumK(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[-1 for _ in range(k + 1)] for _ in range(n)] # DP Array for memoization
    def helper(idx: int, target: int) -> int:
        if target == 0: return 1
        if idx == 0: return 1 if arr[0] == target else 0
        if target < 0: return 0
        if dp[idx][target] != -1: return dp[idx][target] # If answer already in dp array => return it

        pick = helper(idx - 1, target - arr[idx])
        notPick = helper(idx - 1, target)

        dp[idx][target] = pick + notPick # Store answer in the dp array
        return dp[idx][target]
    
    return helper(n - 1, k)

if __name__ == '__main__':
    testCases = [
        ([2, 3, 5, 16, 8, 10], 10),   # 3
        ([1, 2, 3, 4, 5], 5),         # 3
        ([2,2,2,2], 4),               # 6
    ]

    for i, inp in enumerate(testCases):
        arr, k = inp
        print(f'TestCase {i}: i/p: arr={arr}, k={k}; o/p: {countSubsetsWithSumK(arr, k)}')