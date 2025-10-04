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
    @intuition:
        1. S1 + S2 = sum(arr)
        2. S1 - S2 = diff => S2 = S1 - diff
        3. => Substitute in 1: 
                S1 + S1 - diff = sum(arr)
            => S1 = (sum(arr) + diff) // 2

        i.e., if we find if there exists a partition in the array whose elements sum to S1 as derived, then automatically the remaining elements sum to S2.

        Therefore, the question boils down to counting the partition in the array with sum S1.
"""
def countPartitionsWithGivenDiff(arr: List[int], diff: int) -> int:
    n = len(arr)
    target = diff + sum(arr)
    if target % 2 == 1: # If (diff + SUM(arr)) is not even, then it means the partition does not exist at all because S1 is (diff + SUM(arr)) / 2 and all the elements are integers, so S1 should be an integer
        return 0
    target //= 2 # S1

    def countSubsetWithGivenSum(idx: int, target: int) -> int:
        # Base Cases
        if target == 0: return 1 # If target sum achieved, increase count
        if idx == 0: return 1 if arr[0] == target else 0 # If idx == 0 => target sum achieved only if target == arr[0] or target == 0
        if target < 0: return 0 # Already exceeded target sum, so not valid partition!

        pick = 0
        if arr[idx] != 0:
            # Choice 1: Pick the current element
            pick = countSubsetWithGivenSum(idx - 1, target - arr[idx]) 
        # Choice 2: Don't pick the current element
        notPick = countSubsetWithGivenSum(idx - 1, target)

        # Return the total count in both the paths
        return pick + notPick
    
    zeros = 0
    for num in arr:
        if num == 0: zeros += 1
    combos = 2 ** zeros
    return countSubsetWithGivenSum(n - 1, target) * combos


if __name__ == '__main__':
    testCases = [
        ([1, 1, 2, 3], 1),       # 3
        ([1, 2, 3, 4], 2) ,      # 2
        ([2, 0, 0, 0, 1], 1),    # 8
    ]

    for i, inp in enumerate(testCases):
        arr, diff = inp
        print(f'TestCase {i}: i/p: arr={arr}, diff={diff}; o/p: {countPartitionsWithGivenDiff(arr, diff)}')