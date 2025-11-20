# Link: https://leetcode.com/problems/longest-increasing-subsequence/

"""
    @question:
        Given an integer array nums, return the length of the longest strictly increasing subsequence.

        Example 1:
            Input: nums = [10,9,2,5,3,7,101,18]
            Output: 4
            Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    
        ---------------------------------------------------
            
        Example 2:
            Input: nums = [0,1,0,3,2,3]
            Output: 4
        
        ----------------------------------------------------

        Example 3:
            Input: nums = [7,7,7,7,7,7,7]
            Output: 1
    
    --------------------------------------------------------------

        Constraints:
            1 <= nums.length <= 2500
            -104 <= nums[i] <= 104
"""
from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    seq = [nums[0]]
    for num in nums[1:]:
        if seq[-1] < num:
            seq.append(num)
        else:
            idx = lowerBound(seq, num)
            seq[idx] = num

    return len(seq)

def lowerBound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    ans = -1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    
    return ans

if __name__ == '__main__':
    testCases = [
        [10,9,2,5,3,7,101,18],  # 4
        [0,1,0,3,2,3],  # 4
        [7,7,7,7,7,7,7],    # 1
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}: i/p: nums={nums}; o/p: {lengthOfLIS(nums)}")