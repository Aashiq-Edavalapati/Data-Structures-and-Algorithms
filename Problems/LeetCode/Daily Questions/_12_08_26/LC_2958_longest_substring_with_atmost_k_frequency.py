# Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

from typing import List

def maxSubarrayLength(nums: List[int], k: int) -> int:
    i = 0
    freq = {}
    n = len(nums)
    maxLen = 1
    for j in range(n):
        freq[nums[j]] = freq.get(nums[j], 0) + 1

        while freq[nums[j]] > k:
            freq[nums[i]] -= 1
            i += 1
        
        maxLen = max(maxLen, j - i + 1)
    
    return maxLen

if __name__ == "__main__":
    testCases = [
        ([1,2,3,1,2,3,1,2], 2), # 6
        ([1,2,1,2,1,2,1,2], 1), # 2
        ([5,5,5,5,5,5,5], 4), # 4
    ]

    for i, (nums, k) in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}, k={k}; o/p: {maxSubarrayLength(nums, k)}")