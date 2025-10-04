"""
    @question:
        Given an array arr of n integers and an integer diff, count the number of ways to partition the array into two subsets S1 and S2 such that:

        |S1| - |S2| = diff and S1 ≥ S2
        Where |S1| and |S2| are sum of Subsets S1 and S2 respectively.

        Return the result modulo 1e9 + 7.


        Examples:

            Input: arr = [1, 1, 2, 3], diff = 1
            Output: 3
            Explanation: The subsets are [1, 2] and [1, 3], [1, 3] and [1, 2], [1, 1, 2] and [3].
        ------------------------------------------------------------------------------------------
            Input: arr = [1, 2, 3, 4], diff = 2
            Output: 2
            Explanation: The subsets are [1, 3] and [2, 4], [1, 2, 3] and [4].
        
        Constraints:
            1 <= n <= 200
            0 <= d <= 104
            0 <= arr[i] <= 50
"""

from typing import List
"""
    1. S1 + S2 = sum(arr)
    2. S1 - S2 = diff => S2 = S1 - diff
    3. => Substitute in 1: 
            S1 + S1 - diff = sum(arr)
         => S1 = (sum(arr) + diff) // 2
"""

def countPartitionsWithGivenDiff(arr: List[int], diff: int) -> int:
    n = len(arr)
    target = diff + sum(arr)
    if target % 2 == 1:
        return 0
    target //= 2
    prev = [0 for _ in range(target + 1)]
    prev[0] = 1
    if arr[0] <= target: prev[arr[0]] = 1

    for idx in range(1, n):
        curr = [0 for _ in range(target + 1)]
        for tar in range(1, target + 1):
            pick = 0
            if arr[idx] != 0 and tar - arr[idx] >= 0:
                pick = prev[tar - arr[idx]]
            notPick = prev[tar]

            curr[tar] = pick + notPick
        prev = curr
    
    return prev[target] * (2 ** sum(1 for num in arr if num == 0))

if __name__ == '__main__':
    testCases = [
        ([1, 1, 2, 3], 1),      # 3
        ([1, 2, 3, 4], 2) ,      # 2
        ([2, 0, 0, 0, 1], 1),    # 8
    ]

    for i, inp in enumerate(testCases):
        arr, diff = inp
        print(f'TestCase {i}: i/p: arr={arr}, diff={diff}; o/p: {countPartitionsWithGivenDiff(arr, diff)}')