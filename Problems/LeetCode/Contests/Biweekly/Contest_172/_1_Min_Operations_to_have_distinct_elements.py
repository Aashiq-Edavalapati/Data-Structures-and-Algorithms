# Link: https://leetcode.com/contest/biweekly-contest-172/problems/minimum-number-of-operations-to-have-distinct-elements/

"""
    @question:
        You are given an integer array nums.

        In one operation, you remove the first three elements of the current array. If there are fewer than three elements remaining, all remaining elements are removed.

        Repeat this operation until the array is empty or contains no duplicate values.

        Return an integer denoting the number of operations required.

    ================================================================
    ================================================================    

        Example 1:
            Input: nums = [3,8,3,6,5,8]
            Output: 1
            Explanation:
                In the first operation, we remove the first three elements. The remaining elements [6, 5, 8] are all distinct, so we stop. Only one operation is needed.

        ================================================================

        Example 2:
            Input: nums = [2,2]
            Output: 1
            Explanation:
                After one operation, the array becomes empty, which meets the stopping condition.

        ================================================================

        Example 3:
            Input: nums = [4,3,5,1,2]
            Output: 0
            Explanation:
                All elements in the array are distinct, therefore no operations are needed.

    ================================================================
    ================================================================

        Constraints:

        1 <= nums.length <= 105
        1 <= nums[i] <= 105

        Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""
from typing import List
from collections import defaultdict

def minOperations(nums: List[int]) -> int:
    n = len(nums)
    if n < 3: return 0 if len(set(nums)) == n else 1

    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1

    ops = 0
    for l in range(0, n, 3):
        if len(freq) == n - l: return ops
        if n - l < 3: return ops + 1
        for i in range(l, l + 3):
            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]
        ops += 1
        
    return ops