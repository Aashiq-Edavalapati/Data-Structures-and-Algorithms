from typing import List
'''
    @question:
        A ninja has planned a n-day training schedule. Each day he has to perform one of three activities - running, stealth training, or fighting practice. The same activity cannot be done on two consecutive days and the ninja earns a specific number of merit points, based on the activity and the given day.

        Given a n x 3-sized points, where points[i][0], points[i][1], and points[i][2], represent the merit points associated with running, stealth and fighting practice, on the (i + 1)th day respectively. Return the maximum possible merit points that the ninja can earn.
'''
'''
    @examples:
        Input: points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
        Output: 210
        Explanation:
            Day 1: fighting practice = 70
            Day 2: stealth training = 50
            Day 3: fighting practice = 90
            Total = 70 + 50 + 90 = 210
            This gives the optimal points.
------------------------------------------------------------------------------------
        Input: points = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
        Output: 290
        Explanation:
            Day 1: running = 70
            Day 2: stealth training = 20
            Day 3: running = 200
            Total = 70 + 20 + 200 = 290
            This gives the optimal points.
'''

"""
    @method
    3 steps:
        1. Represent everything in terms of indices.
            0, 1, ...., n - 1 => day index of the array
            0, 1, 2 => Col index in a day
        2. Do all possible stuffs acc. to the problem statement. [f(day, prev)]
            Pick one of the 3 in each day: points[day][0] + f(day - 1, 0) or points[day][1] + f(day - 1, 1) or points[day][2] + f(day - 1, 2)
        3. Max => Max(all stuffs)
            Max((points[day][0] + f(day - 1, 0)), (points[day][1] + f(day - 1, 1)), (points[day][2] + f(day - 1, 2)))
"""
def ninjaTraining(points: List[List[int]], dp: List[List[int]]) -> int:
    def helper(day: int, prev: int) -> int:
        if day == 0:
            maxScore = 0
            for task in range(3):
                if task != prev:
                    maxScore = max(maxScore, points[day][task])
            return maxScore
        if dp[day][prev] != -1: return dp[day][prev]

        dp[day][prev] = 0
        for task in range(3):
            if task != prev:
                dp[day][prev] = max(dp[day][prev], points[day][task] + helper(day - 1, task))
                
        return dp[day][prev]
    
    return helper(len(points) - 1, 3)

if __name__ == '__main__':
    testCases = [
        [[10, 40, 70], [20, 50, 80], [30, 60, 90]],   # 210
        [[70, 40, 10], [180, 20, 5], [200, 60, 30]],  # 290
        [[20, 10, 10], [20, 10, 10], [20, 30, 10]],   # 60
        [[1, 2, 3], [3, 2, 1], [10, 20, 30]],         # 36
    ]
    for i, points in enumerate(testCases):
        dp = [[-1 for _ in range(4)]] * len(points)
        print(f'TestCase {i}: i/p: {points} o/p: {ninjaTraining(points, dp)}')