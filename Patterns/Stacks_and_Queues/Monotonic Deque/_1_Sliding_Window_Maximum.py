# Link: https://leetcode.com/problems/sliding-window-maximum/

"""
    @question(LC 239):
        You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

        Return the max sliding window.

        ================================================================
        ================================================================

        Example 1:

            Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
            Output: [3,3,5,5,6,7]
            Explanation: 
                Window position                Max
                ---------------               -----
                [1  3  -1] -3  5  3  6  7       3
                1 [3  -1  -3] 5  3  6  7       3
                1  3 [-1  -3  5] 3  6  7       5
                1  3  -1 [-3  5  3] 6  7       5
                1  3  -1  -3 [5  3  6] 7       6
                1  3  -1  -3  5 [3  6  7]      7

        ================================================================

        Example 2:
            Input: nums = [1], k = 1
            Output: [1]
        
    ================================================================
    ================================================================

        Constraints:
            1 <= nums.length <= 105
            -104 <= nums[i] <= 104
            1 <= k <= nums.length
"""
from typing import List

def slidingWindowMax(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    dq = []
    ans = []
    for i in range(n):
        if dq and i - dq[0] >= k: dq.pop(0)
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1: ans.append(nums[dq[0]])
    
    return ans


if __name__ == '__main__':
    testCases = [
        ([1,3,-1,-3,5,3,6,7], 3), # [3,3,5,5,6,7]
        ([1], 1), # 1
    ]

    for i, testCase in enumerate(testCases):
        nums, k = testCase
        print(f"TestCase {i}:- i/p: nums={nums}, k={k}; o/p: {slidingWindowMax(nums, k)}")