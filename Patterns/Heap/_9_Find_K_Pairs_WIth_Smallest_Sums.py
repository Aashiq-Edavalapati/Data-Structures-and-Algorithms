# Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

"""
    @question:
        You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

        Define a pair (u, v) which consists of one element from the first array and one element from the second array.

        Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Example 1:
            Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
            Output: [[1,2],[1,4],[1,6]]
            Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

        -------------------------------------------------------------------------------
            
        Example 2:
            Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
            Output: [[1,1],[1,1]]
            Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Constraints:
            1 <= nums1.length, nums2.length <= 105
            -109 <= nums1[i], nums2[i] <= 109
            nums1 and nums2 both are sorted in non-decreasing order.
            1 <= k <= 104
            k <= nums1.length * nums2.length
"""
from typing import List
import heapq

def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
        @intuition:
            @info.: 
                - Both the arrays are sorted.
                m = len(nums1), n = len(nums2)
            @Requirement: We want k pairs with the smallest sums. 
            @Thinking:
                @BruteForce:
                    - Most naive way would be to generate all the pairs, sort them by sum and first k pairs. 
                    - Complexity:- O((m * n) * log(m * n))
                @Improved BruteForce:
                    @Hint:
                        - Since we want first k .... => Obvious hint for using heap
                    - Same idea, but instead of sorting we can heap to reduce complexity to O(k * log(m * n))
                @Optimal:
                    @Hint: 
                        - If you think we already used heap and how do we think of a much optimal solution. Observe the fact that we have not utilized the fact that the arrays are sorted.
                    - If we observe the smallest sum pair will always be (nums1[0], nums2[0]). So, this will the 1st pair in all the cases.
                    - Now visualize the following grid for better understanding:
                  ind →          0   1   2
                  nums2 →        2   4   6
                                ------------
                        0    1  |  3   5   7                    
                        1    7  |  9  11  13                 Each cell is sum of a pair
                        2    11 | 13  15  17
                            ↓
                            nums1
                        * We know that we always start from cell (0, 0).
                    - At each cell (i, j); the obvious next smallest will be either of the previously generated pairs or one of (i + 1, j) and (i, j + 1). Because, both the arrays are sorted remember?
                    - So, we need not go too far and generate all the pairs at a time.
                    - We can move 1 step at a time in 2 ways as mentioned above. That (i + 1, j) and (i, j + 1) thingy.
                    - Now, we've got another problem! After adding (i, j), the next smallest can be either one of the previously generated pair or one of the above two next pairs. So, how do we get the next smallest out of these filtered pairs? => Heap
                    - Also, if you observe the grid, it might be possible that we can end up in the same cell twice. So, we need a set to make sure we add each pair only once into the heap.

                    - We repeat the process till we get k pairs.
    """
    m, n = len(nums1), len(nums2)
    cnt = 0
    pairs = []
    visited = set()
    minHeap = [(nums1[0] + nums2[0], 0, 0)]
    while cnt < k and minHeap:
        nxtSum, i, j = heapq.heappop(minHeap)
        if i + 1 < m:
            if (i + 1, j) not in visited:
                n1 = nums1[i + 1] + nums2[j]
                heapq.heappush(minHeap, (n1, i + 1, j))
                visited.add((i + 1, j))
        if j + 1 < n:
            if (i, j + 1) not in visited:
                n2 = nums1[i] + nums2[j + 1]
                heapq.heappush(minHeap, (n2, i, j + 1))
                visited.add((i, j + 1))
        
        pairs.append([nums1[i], nums2[j]])
        cnt += 1
    
    return pairs

if __name__ == '__main__':
    testCases = [
        [[1,7,11], [2,4,6], 3],
        [[1,1,2], [1,2,3], 2]
    ]

    for i, testCase in enumerate(testCases):
        nums1, nums2, k = testCase
        print(f"TestCase {i}:- i/p: nums1={nums1}, nums2={nums2} k={k}; o/p: {kSmallestPairs(nums1, nums2, k)}")