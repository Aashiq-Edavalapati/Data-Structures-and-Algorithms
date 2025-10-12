"""
    @question:
        Given a rod of length N inches and an array price[] where price[i] denotes the value of a piece of rod of length i inches (1-based indexing). Determine the maximum value obtainable by cutting up the rod and selling the pieces. Make any number of cuts, or none at all, and sell the resulting pieces.

        Examples:
            Input: price = [1, 6, 8, 9, 10, 19, 7, 20], N = 8
            Output: 25
            Explanation: Cut the rod into lengths of 2 and 6 for a total price of 6 + 19= 25.
        ----------------------------------------------------------------------------------------
            Input: price = [1, 5, 8, 9], N = 4
            Output: 10
            Explanation: Cut the rod into lengths of 2 and 2 for a total price of 5 + 5 = 10.
        
        
        Constraints:
            1 ≤ N ≤ 1000
            1 ≤ price[i] ≤ 105
"""

from typing import List

def rodCutting(price: List[int], n: int) -> int:
    def solve(curr: int, rem: int):
        # Base Cases
        # 1. rem == 0 => Sum of sizes of all the picked pieces till now sum to the original size => Stop going further
        # 2. curr > rem => We've taken more than what is required => Stop
        if rem == 0 or curr > rem:
            return 0

        # Choice 1: Pick the current partition size(We can select the same sized partition any number of times => don't change curr in the further recursive call)
        pick = price[curr - 1] + solve(curr, rem - curr)
        # Choice 2: Don't pick the current partition size => Move to next partition size
        notPick = solve(curr + 1, rem)

        # Return the max of both the choices
        return max(pick, notPick)
    
    return solve(1, n)

if __name__ == '__main__':
    testCases = [
        ([1, 6, 8, 9, 10, 19, 7, 20], 8),    # 25
        ([1, 5, 8, 9], 4),                   # 10
        ([5, 5, 8, 9, 10, 17, 17, 20], 8) ,  # 40
        ([42, 68, 35, 1, 70], 5),            # 210
        ([25, 79, 59, 63, 65, 6, 46, 82], 8) # 316
    ]

    for i, inp in enumerate(testCases):
        price, n = inp
        print(f'TestCase {i}: i/p: price={price}, n={n}; o/p: {rodCutting(price, n)}')