"""
    @question:
        You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

        Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

        For Example :
            If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
        
        Constraints:
            1 <= T <= 5
            1 <= N <= 10^3
            0 <= ARR[i] <= 10^9
            0 <= K <= 10^3

        Sample Input 1:
            2
            4 5
            4 3 2 1
            5 4
            2 5 1 6 7
        Sample Output 1:
            true
            false
        Explanation For Sample Input 1:
            In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
            In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
        
        
        Sample Input 2:
            2
            4 4
            6 1 2 1
            5 6
            1 7 2 9 10
        Sample Output 2:
            true
            false
        Explanation For Sample Input 2:
            In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
            In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.
"""

from typing import List


def subSetSumToTarget(arr: List[int], target: int) -> int:
    n = len(arr)
    def helper(ind, target):
        if target == 0: return True
        if ind == 0: return arr[0] == target

        pick = helper(ind - 1, target - arr[ind])
        notPick = helper(ind - 1, target)

        return pick or notPick

    return helper(n - 1, target)

if __name__ == '__main__':
    testCases = [
        ([1, 2, 7, 3], 6),      # True
        ([2, 3, 5], 6),         # False
        ([7, 54, 4, 12, 15, 5], 9) # True
    ]

    for i, inp in enumerate(testCases):
        arr, target = inp
        print(f'TestCase {i}: i/p: arr={arr}, target={target}; o/p: {subSetSumToTarget(arr, target)}')