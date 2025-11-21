# Link: https://leetcode.com/problems/largest-divisible-subset/

"""
    @question:
        Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

        answer[i] % answer[j] == 0, or
        answer[j] % answer[i] == 0
        If there are multiple solutions, return any of them.

--------------------------------------------------------------------------------------------

        Example 1:
            Input: nums = [1,2,3]
            Output: [1,2]
            Explanation: [1,3] is also accepted.

        ------------------------------------------
            
        Example 2:
            Input: nums = [1,2,4,8]
            Output: [1,2,4,8]

-----------------------------------------------------------------------------------------

        Constraints:
            1 <= nums.length <= 1000
            1 <= nums[i] <= 2 * 109
            All the integers in nums are unique.
"""
from typing import List

def largestDivisibleSubset(nums: List[int]) -> List[int]:
    n = len(nums)
    largest = []
    path = []
    nums.sort()
    def helper(idx: int, prev: int, path: List[int]) -> None:
        nonlocal largest
        if len(path) > len(largest):
            largest = path[:]
        if idx == n:
            return

        if prev == -1 or nums[idx] % prev == 0:
            path.append(nums[idx])
            helper(idx + 1, nums[idx], path)
            path.pop()
        helper(idx + 1, prev, path)

    helper(0, -1, path)
    return largest

if __name__ == '__main__':
    testCases = [
        [1,2,3], # [1, 2]
        [1,2,4,8], # [1,2,4,8]
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o.p: {largestDivisibleSubset(nums)}")