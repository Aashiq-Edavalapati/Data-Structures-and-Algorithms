# Link: https://leetcode.com/problems/two-best-non-overlapping-events/

# Patterns: Greedy, Suffix Array(DP), Binary Search

"""
    @question:
        You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

        Return this maximum sum.

        Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

    =============================================================
    =============================================================

        Example 1:
            Input: events = [[1,3,2],[4,5,2],[2,4,3]]
            Output: 4
            Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

        =============================================================

        Example 2:
            Input: events = [[1,3,2],[4,5,2],[1,5,5]]
            Output: 5
            Explanation: Choose event 2 for a sum of 5.

        =============================================================

        Example 3:
            Input: events = [[1,5,3],[1,5,1],[6,6,5]]
            Output: 8
            Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
        
    =============================================================
    =============================================================

        Constraints:
            2 <= events.length <= 105
            events[i].length == 3
            1 <= startTimei <= endTimei <= 109
            1 <= valuei <= 106
"""
from typing import List

def searchNextValidEvent(events: List[List[int]], l: int, end: int) -> int:
    r = len(events) - 1
    res = -1
    while l <= r:
        mid = l + (r - l) // 2
        if events[mid][0] > end:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return res

def maxTwoEvents(events: List[List[int]]) -> int:
    n = len(events)
    events.sort(key=lambda x : x[0])
    maxValue = 0

    suffixMax = [0] * n
    suffixMax[-1] = events[-1][2]
    for i in range(n - 2, -1, -1):
        suffixMax[i] = max(events[i][2], suffixMax[i + 1])

    for i in range(n):
        _, end, val = events[i]
        idx = i
        maxValue = max(maxValue, val)
        nextValidEventIdx = searchNextValidEvent(events, idx + 1, end)
        if nextValidEventIdx != -1:
            maxValue = max(maxValue, val + suffixMax[nextValidEventIdx])
            idx = nextValidEventIdx

    return maxValue
if __name__ == '__main__':
    testCases = [
        [[1,3,2],[4,5,2],[2,4,3]], # 4
        [[1,3,2],[4,5,2],[1,5,5]], # 5
        [[1,5,3],[1,5,1],[6,6,5]], # 8
        [[66,97,90],[98,98,68],[38,49,63],[91,100,42],[92,100,22],[1,77,50],[64,72,97]], # 165
    ]

    for i, events in enumerate(testCases):
        print(f"TestCase {i}:- i/p: events={events}; o/p: {maxTwoEvents(events)}")