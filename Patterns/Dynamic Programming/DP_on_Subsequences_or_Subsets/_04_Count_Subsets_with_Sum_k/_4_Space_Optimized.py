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
    # Initialize the row array
    prevRow = [0 for _ in range(k + 1)]
    # 1. Base Cases
    prevRow[0] = 1 # target == 0
    if arr[0] <= k: prevRow[arr[0]] = 1 # target == arr[0]

    # 2. Start iterating from bottom to up
    for idx in range(1, n): # idx == 0 is base case => Start from 1
        # Temporary array to store current idx row in dp array in bottom up solution
        temp = [0 for _ in range(k + 1)]
        temp[0] = 1 # Base Case (target == 0)
        for target in range(1, k + 1):
            pick = 0
            if target - arr[idx] >= 0: # Index bound condition
                pick = prevRow[target - arr[idx]]
            notPick = prevRow[target]

            temp[target] = pick + notPick
        prevRow = temp # Update the previous row
    
    return prevRow[k]

if __name__ == '__main__':
    testCases = [
        ([2, 3, 5, 16, 8, 10], 10),   # 3
        ([1, 2, 3, 4, 5], 5),         # 3
        ([2,2,2,2], 4),               # 6
    ]

    for i, inp in enumerate(testCases):
        arr, k = inp
        print(f'TestCase {i}: i/p: arr={arr}, k={k}; o/p: {countSubsetsWithSumK(arr, k)}')