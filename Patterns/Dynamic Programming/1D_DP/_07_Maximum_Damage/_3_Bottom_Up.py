# Link: https://leetcode.com/problems/maximum-total-damage-with-spell-casting

"""
    @question:
        A magician has various spells.
        You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.
        It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
        Each spell can be cast only once.
        Return the maximum possible total damage that a magician can cast.
        
        Example 1:
            Input: power = [1,1,3,4]
            Output: 6
            Explanation:
                The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.
        --------------------------------------------------------------------------------------------------------
        Example 2:
            Input: power = [7,1,6,6]
            Output: 13
            Explanation:
                The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.
    
    ------------------------------------------------------------------------------------------------------------

        Constraints:
            1 <= power.length <= 105
            1 <= power[i] <= 109
"""

from typing import List

"""

"""
def maximumTotalDamage(power: List[int]) -> int:
    freq = {}
    for num in power:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    power = sorted(list(set(power)))
    n = len(power)
    dp = [-1] * n
    
    dp[n - 1] = power[-1] * freq[power[-1]] # Initialize DP table
    for idx in range(n - 2, -1, -1): # n -1 is base case => Start from n - 2
        curr = power[idx]
        # Find next index if we pick curr
        nextIndex = nextIndex = idx + 1 if idx + 1 < n and power[idx + 1] > curr + 2 else idx + 2 if idx + 2 < n and  power[idx + 2] > curr + 2 else idx + 3
        pick = curr * freq[curr]
        if -1 < nextIndex < n:
            pick += dp[nextIndex] # Replace f(nextIndex) -> dp[nextIndex]
        notPick = dp[idx + 1] # Replace f(idx + 1) -> dp[idx + 1]

        dp[idx] = max(pick, notPick) # Replace return value of f(idx) -> dp[idx]

    return dp[0] # Replace f(0) -> dp[0]


if __name__ == '__main__':
    testCases = [
        [1,1,3,4],      # 6
        [7,1,6,6],      # 13
        [23,10,9,34,6,34,4,20,7,6,34,27,17,12,11,11,17,21,8,21,22,22,29,7,14,8,25,10,9,22,27,23,6,16,23,15,10,30,21,4,26,11,32,18,3,24,11,13,23,20],            # 434
        [5,58,45,54,60,6,34,26,3,64,47,58,13,31,41,32,49,10,51,27,12,24,37,15,11,29,6,41,10,61,17,6,23,36,63,58,50,64,55,52,46,13,33,64,27,41,65,27,11,27,59,53,60,37,66,10,28,32,38,26,9,45,55,9,48,22,22,61,62,8,41,14,23,61,40,40,5,42,60,4,55,50,30,3,58,33,27,25,6,32,8,33,16,34,20,14,7,19,22],       # 1652
    ]

    for i, power in enumerate(testCases):
        print(f'TestCase {i}: i/p: power={power}; o/p: {maximumTotalDamage(power)}')