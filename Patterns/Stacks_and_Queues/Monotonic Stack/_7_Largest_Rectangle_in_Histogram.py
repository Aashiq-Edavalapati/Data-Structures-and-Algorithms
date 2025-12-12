# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

"""
    @question:
        Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Example 1:
            Input: heights = [2,1,5,6,2,3]
            Output: 10
            Explanation: The above is a histogram where width of each bar is 1.
            The largest rectangle is shown in the red area, which has an area = 10 units.

        -------------------------------------------------------------------------------

        Example 2:
            Input: heights = [2,4]
            Output: 4

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------    

        Constraints:
            1 <= heights.length <= 105
            0 <= heights[i] <= 104
"""
from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stk = []
    maxArea = 0
    n = len(heights)
    for i in range(n):
        while stk and heights[stk[-1]] > heights[i]:
            idx = stk.pop()
            w = i - idx
            maxArea = max(maxArea, w * heights[idx])

        stk.append(i)

    while stk:
        idx = stk.pop()
        w = n - idx
        maxArea = max(maxArea, w * heights[idx])

    return maxArea

if __name__ == '__main__':
    testCases = [
        [2,1,5,6,2,3], # 10
        [2,4], # 4
        [2,1,5,5,5,5,6,2,3], # 25
    ]

    for i, heights in enumerate(testCases):
        print(f"TestCase {i}:- i/p: heights={heights}; o/p: {largestRectangleArea(heights)}")