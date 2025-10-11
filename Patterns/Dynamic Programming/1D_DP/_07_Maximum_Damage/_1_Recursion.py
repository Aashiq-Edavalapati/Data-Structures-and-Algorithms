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
    @intuition:
        Since, we are trying to maximize the power, the obvious thought that comes to our is mind is to think greedily. But, since there is no uniformity, like we are prohibited to take some elements based on the current picked element, greedy will fail! Best way to confirm this is by taking an example and trying out.
        For example, take [1, 5, 5, 6]. If we use greedy on this. Then we sort in descending order => [6, 5, 5, 1]. The greedy answer is 6 + 1 = 7, whereas the actual answer is 5 + 5 + 1 = 11. => It clearly shows that greedy fails here.

        => Obvious choice, try out all the possible valid combinations and find maximum of those. => Recursion => DP

        1. Since, we are not allowed to pick curr - 2, curr - 1, curr + 1, curr + 2 and we're trying to maximize the result, we obviously choose all the occurences of curr if we pick curr! => We can pre-calculate frequency of all elements and remove duplicates

        2. If we leave the array as is, then we have to check for validity for next index in both the directions! Which is very difficult! So, Obvious choice is to sort the array. => We eliminate checking for curr - 2 and curr - 1 and we can concentrate only on curr + 1 and curr + 2

        3. If we pick curr => damage += curr * freq[curr] and the next element should be > curr + 2

        Therefore, Algorithm:
            i. Find frequency of each element!
            ii. Remove duplicates and sort the array
            iii. Start simulating, at every recursive call, either pick or not pick the current element.
            iv. If picked, then next index should be of the element that is > curr + 2.
            v. Otherwise, idx + 1
"""
def maximumTotalDamage(power: List[int]) -> int:
    freq = {}
    # Calculate frequencies of each element
    for num in power:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Remove duplicates and sort the array
    power = sorted(list(set(power)))
    n = len(power)
    
    def solve(idx: int) -> int:
        # Base Cases
        if idx >= n: # If not a valid index, we've reached the end => Return 0
            return 0
        if idx == n - 1: # If reached end => There are no further elements to check, so we pick the curr
            return power[idx] * freq[power[idx]]
        

        curr = power[idx]
        # Compute next index to choose if pick curr
        nextIndex = idx + 1 if idx + 1 < n and power[idx + 1] > curr + 2 else idx + 2 if idx + 2 < n and  power[idx + 2] > curr + 2 else idx + 3

        # Choice 1: Pick the current element
        pick = curr * freq[curr] + solve(nextIndex)
        # Choice 2: Don't pick the current element
        notPick = solve(idx + 1) 

        # Return max of both the choices
        return max(pick, notPick)
    
    return solve(0)


if __name__ == '__main__':
    testCases = [
        [1,1,3,4],      # 6
        [7,1,6,6],      # 13
        [23,10,9,34,6,34,4,20,7,6,34,27,17,12,11,11,17,21,8,21,22,22,29,7,14,8,25,10,9,22,27,23,6,16,23,15,10,30,21,4,26,11,32,18,3,24,11,13,23,20],            # 434
        [5,58,45,54,60,6,34,26,3,64,47,58,13,31,41,32,49,10,51,27,12,24,37,15,11,29,6,41,10,61,17,6,23,36,63,58,50,64,55,52,46,13,33,64,27,41,65,27,11,27,59,53,60,37,66,10,28,32,38,26,9,45,55,9,48,22,22,61,62,8,41,14,23,61,40,40,5,42,60,4,55,50,30,3,58,33,27,25,6,32,8,33,16,34,20,14,7,19,22],       # 1652
    ]

    for i, power in enumerate(testCases):
        print(f'TestCase {i}: i/p: power={power}; o/p: {maximumTotalDamage(power)}')