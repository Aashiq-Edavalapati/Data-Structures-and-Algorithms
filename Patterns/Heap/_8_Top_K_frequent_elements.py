# Link: https://leetcode.com/problems/top-k-frequent-elements/

"""
    @question(LC 347):
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    ====================================================================
    ====================================================================

        Example 1:
            Input: nums = [1,1,1,2,2,3], k = 2
            Output: [1,2]

        ====================================================================

        Example 2:
            Input: nums = [1], k = 1
            Output: [1]

        ====================================================================

        Example 3:
            Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
            Output: [1,2]

    ====================================================================
    ====================================================================

        Constraints:
            1 <= nums.length <= 105
            -104 <= nums[i] <= 104
            k is in the range [1, the number of unique elements in the array].
            It is guaranteed that the answer is unique.
"""
import heapq
from typing import List
from collections import defaultdict

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    
    maxHeap = []
    for num, f in freq.items():
        heapq.heappush(maxHeap, (-f, num))
    
    topK = []
    for _ in range(k):
        topK.append(heapq.heappop(maxHeap)[1])
    
    return topK

if __name__ == '__main__':
    testCases = [
        ([1,1,1,2,2,3], 2), # [1, 2]
        ([1], 1), # [1]
        ([1,2,1,2,1,2,3,1,3,2], 2), # [1, 2] 
    ]

    for i, testCase in enumerate(testCases):
        arr, k = testCase
        print(f"TestCase {i}:- i/p: arr={arr}, k={k}; o/p: {topKFrequent(arr, k)}")