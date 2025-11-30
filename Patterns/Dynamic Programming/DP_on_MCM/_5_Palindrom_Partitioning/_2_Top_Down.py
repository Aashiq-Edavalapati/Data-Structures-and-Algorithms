# Link: https://leetcode.com/problems/palindrome-partitioning-ii/

"""
    @question:
        Given a string s, partition s such that every substring of the partition is a palindrome.

        Return the minimum cuts needed for a palindrome partitioning of s.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Example 1:
            Input: s = "aab"
            Output: 1
            Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
    
        -------------------------------------------------------------------------------

        Example 2:
            Input: s = "a"
            Output: 0
        
        -------------------------------------------------------------------------------

        Example 3:
            Input: s = "ab"
            Output: 1
        
    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Constraints:
            1 <= s.length <= 2000
            s consists of lowercase English letters only.
"""

def minCuts(s: str) -> int:
    n = len(s)
    dp = [-1 for _ in range(n)] # Initialize DP Table
    def helper(i: int) -> int:
        if i == n: return 0
        if dp[i] != -1: return dp[i] # IF result was already stored, then return

        minCut = float('inf')
        for j in range(i, n):
            if isPalindrome(i, j, s):
                cuts = 1 + helper(j + 1)
                minCut = min(minCut, cuts)
        
        dp[i] = minCut # Store the result in DP Table
        return minCut

    return helper(0) - 1

def isPalindrome(i: int, j: int, s: str) -> bool:
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    
    return True

if __name__ == '__main__':
    testCases = [
        "aab", # 1
        "a", # 0
        "ab", # 1
        "abaaba", # 0
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {minCuts(s)}")