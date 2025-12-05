from typing import List

def maxSubarraySum(nums: List[int]) -> int:
    maxEnding, res = nums[0], nums[0]
    for num in nums:
        maxEnding = max(maxEnding + num, maxEnding)
        res = max(res, maxEnding)

    return res

def maxSubarraySum2(nums: List[int]) -> int:
    maxEnding, res = nums[0], nums[0]
    for i in range(1, len(nums)):
        maxEnding += nums[i]
        maxEnding = max(maxEnding, nums[i])
        res = max(res, maxEnding)
    
    return res