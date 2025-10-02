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
            0 <= arr[i] <= 103
            1 <= K <= 103
"""

""" Method 1 """
def countSubsetsWithSumK(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]
    # "Base Cases: "
    for row in dp:  # 1. target == 0 => 1
        row[0] = 1
    if arr[0] <= k: dp[0][arr[0]] = 1 # 2. target == arr[0] => 1
    # 3. Since, there is no negative index, we'll handle 'target < 0' case in the for loop

    for idx in range(1, n): # "idx = 0" is base case => Start from 1
        for target in range(1, k + 1): # "target = 0" is base case => Start from 1
            pick = 0
            if arr[idx] != 0 and target - arr[idx] >= 0: # Check for index bound
                pick = dp[idx - 1][target - arr[idx]]
            notPick = dp[idx - 1][target]

            dp[idx][target] = pick + notPick
    
    zeros = 0
    for num in arr:
        if num == 0: zeros += 1
    combos = 2 ** zeros
    return dp[n - 1][k] * combos

""" Method 2 """
def countSubsetsWithSumK2(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]
    # "Base Cases"
    dp[0][0] = 1 # 1. idx == 0 && target == 0 => 1
    if arr[0] == 0: dp[0][0] = 2  # 2. idx == 0 && target == 0 && arr[0] == 0 => 2
    elif arr[0] <= k: dp[0][arr[0]] = 1  # 3. idx == 0 && target == arr[0] => 1
    # 4. Since, there is no negative index, we'll handle target < 0 in the for loop

    for idx in range(1, n): # 'idx = 0' is base case => Start from 1
        for target in range(k + 1): # 'target = 0' is base case only when 'idx = 0' => Start from 0
            pick = 0
            if target - arr[idx] >= 0: # Handle index bound
                pick = dp[idx - 1][target - arr[idx]]
            notPick = dp[idx - 1][target]

            dp[idx][target] = pick + notPick
    
    return dp[n - 1][k]

if __name__ == '__main__':
    testCases = [
        ([2, 3, 5, 16, 8, 10], 10),   # 3
        ([1, 2, 3, 4, 5], 5),         # 3
        ([2, 2, 2, 2], 4),            # 6
        ([0, 0, 0, 1], 1),            # 8
        ([2, 0, 1, 0, 0, 1], 2)       # 16
    ]

    for i, inp in enumerate(testCases):
        arr, k = inp
        # print(f'TestCase {i}: i/p: arr={arr}, k={k}; o/p: {countSubsetsWithSumK(arr, k)}')
        print(f'TestCase {i}: i/p: arr={arr}, k={k}; o/p: {countSubsetsWithSumK2(arr, k)}')