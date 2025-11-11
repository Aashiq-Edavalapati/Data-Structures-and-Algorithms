# Link: https://leetcode.com/problems/ones-and-zeroes/

"""
    @question:
        You are given an array of binary strings strs and two integers m and n.

        Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

        A set x is a subset of a set y if all elements of x are also elements of y.

    ----------------------------------------------------------------------------------

        Example 1:
            Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
            Output: 4
            Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
                Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
                {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
        
        --------------------------------------------------------------------------------
                
        Example 2:
            Input: strs = ["10","0","1"], m = 1, n = 1
            Output: 2
            Explanation: The largest subset is {"0", "1"}, so the answer is 2.
        
    --------------------------------------------------------------------------

        Constraints:
            1 <= strs.length <= 600
            1 <= strs[i].length <= 100
            strs[i] consists only of digits '0' and '1'.
            1 <= m, n <= 100
"""
from typing import List

def findMaxForm(strs: List[str], m: int, n: int) -> int:
    dp = [[[-1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs))]
    def helper(idx: int, zeros: int, ones: int) -> int:
        if zeros < 0 or ones < 0: return -1
        if idx < 0: return 0
        if zeros == 0 and ones == 0: return 0
        if dp[idx][zeros][ones] != -1: return dp[idx][zeros][ones]

        curr = strs[idx]
        cnt0, cnt1 = curr.count('0'), curr.count('1')
        pick = 1 + helper(idx - 1, zeros - cnt0, ones - cnt1)
        notPick = helper(idx - 1, zeros, ones)

        dp[idx][zeros][ones] = max(pick, notPick)
        return dp[idx][zeros][ones]
    
    return helper(len(strs) - 1, m, n)

if __name__ == '__main__':
    testCases = [
        (["10","0001","111001","1","0"], 5, 3), # 4
        (["10","0","1"], 1, 1), # 2
    ]

    for i, testCase in enumerate(testCases):
        strs, m, n = testCase
        print(f"TestCase {i}: i/p: strs={strs}, m={m}, n={n}; o/p: {findMaxForm(strs, m, n)}")