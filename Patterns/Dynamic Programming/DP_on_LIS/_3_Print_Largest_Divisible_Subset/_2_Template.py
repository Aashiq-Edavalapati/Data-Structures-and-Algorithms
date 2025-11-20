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
    nums.sort()
    dp = [0 for _ in range(n + 1)]
    # Step 1: Build Parent! + DP table
    parent = [i for i in range(n)]
    for idx in range(n):
        for prev in range(idx):
            if nums[idx] % nums[prev] == 0:
                if dp[idx] <= dp[prev] + 1:
                    # Update parent of idx whenever dp[idx] is being updated
                    parent[idx] = prev
                    dp[idx] = dp[prev] + 1
    
    # Step 2: Build sequence
    largest = []
    currIdx = max(range(n), key=lambda i : dp[i])
    while parent[currIdx] != currIdx:
        largest.append(nums[currIdx])
        currIdx = parent[currIdx]        
    largest.append(nums[currIdx])

    return largest[::-1]

if __name__ == '__main__':
    testCases = [
        [1,2,3], # [1, 2]
        [1,2,4,8], # [1,2,4,8]
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o.p: {largestDivisibleSubset(nums)}")