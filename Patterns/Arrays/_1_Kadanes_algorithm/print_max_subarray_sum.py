from typing import List

def maxSubarray(nums: List[int]) -> List[int]:
    maxEnding, maxSum = nums[0], nums[0]

    resStart, resEnd, currStart = 0, 0, 0
    for i in range(1, len(nums)):
        maxEnding += nums[i]
        if nums[i] > maxEnding:
            maxEnding = nums[i]
            currStart = i
        
        if maxEnding > maxSum:
            maxSum = maxEnding
            resStart = currStart
            resEnd = i
    
    return nums[resStart: resEnd + 1]

if __name__ == '__main__':
    testCases = [
        [2, 3, -8, 7, -1, 2, 3],
        [-2, -5, 6, -2, -3, 1, 5, -6]
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {maxSubarray(nums)}")