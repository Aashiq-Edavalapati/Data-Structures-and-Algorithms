# Link: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor, hasNonZero = 0, False

        for num in nums:
            xor ^= num
            if num != 0:
                hasNonZero = True
        
        if xor != 0: return len(nums)

        return len(nums) - 1 if hasNonZero else 0

if __name__ == '__main__':
    sol = Solution()
    testCases = [
        [1,2,3], # 2
        [2,3,4], # 3
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {sol.longestSubsequence(nums)}")