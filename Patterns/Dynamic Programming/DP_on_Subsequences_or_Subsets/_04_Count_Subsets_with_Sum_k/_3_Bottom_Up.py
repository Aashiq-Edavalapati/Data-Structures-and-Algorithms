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
    dp = [[0 for _ in range(k + 1)] for _ in range(n)] # Initialize dp array -> Changing parameters(idx, target)(0 to (n - 1), 0 to target) => Size = n x (target + 1)

    # 1. Base Cases
    for row in dp:
        row[0] = 1 # target == 0
    if arr[0] <= k: dp[0][arr[0]] = 1 # idx == 0 && target == arr[0]
    # Since, index can't be negative target < 0 will be handled in the for loop

    # 2. Start iterating from the bottom to up (From base case to the inital function call)
    #       Replace the recursive calls with dp[][]
    for idx in range(1, n): # Since, idx == 0 is base case start from 1
        for target in range(1, k + 1): # Since target == 0 is base case start from 1
            pick = 0
            if target - arr[idx] >= 0: # Index bound check
                pick = dp[idx - 1][target - arr[idx]]
            notPick = dp[idx - 1][target]

            dp[idx][target] = pick + notPick
    
    return dp[n - 1][k]

if __name__ == '__main__':
    testCases = [
        ([2, 3, 5, 16, 8, 10], 10),   # 3
        ([1, 2, 3, 4, 5], 5),         # 3
        ([2,2,2,2], 4),               # 6
    ]

    for i, inp in enumerate(testCases):
        arr, k = inp
        print(f'TestCase {i}: i/p: arr={arr}, k={k}; o/p: {countSubsetsWithSumK(arr, k)}')