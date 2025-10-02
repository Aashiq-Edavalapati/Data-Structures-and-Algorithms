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
    prevRow = [0 for _ in range(k + 1)]
    prevRow[0] = 1
    if k < arr[0]: prevRow[arr[0]] = 1
    for idx in range(n):
        temp = [0 for _ in range(k + 1)]
        temp[0] = 1
        for target in range(1, k + 1):
            pick = 0
            if target - arr[idx] >= 0:
                pick = prevRow[target - arr[idx]]
            notPick = prevRow[target]

            temp[target] = pick + notPick
        prevRow = temp
    
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