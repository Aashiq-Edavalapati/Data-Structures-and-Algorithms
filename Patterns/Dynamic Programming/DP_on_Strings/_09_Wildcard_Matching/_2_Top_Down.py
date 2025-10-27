# Link: https://leetcode.com/problems/wildcard-matching/

"""
    @question:
        Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).
        The matching should cover the entire input string (not partial).
        
    -------------------------------------------------------------------------------------------
        Example 1:
            Input: s = "aa", p = "a"
            Output: false
            Explanation: "a" does not match the entire string "aa".
    
        ------------------------------------------------------------
            
        Example 2:
            Input: s = "aa", p = "*"
            Output: true
            Explanation: '*' matches any sequence.
        
        -------------------------------------------------------------
            
        Example 3:
            Input: s = "cb", p = "?a"
            Output: false
            Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
        
    --------------------------------------------------------------------------------------------------
            
        Constraints:
            0 <= s.length, p.length <= 2000
            s contains only lowercase English letters.
            p contains only lowercase English letters, '?' or '*'.
"""


def isMatch(s: str, p: str) -> bool:
    n, m = len(s), len(p)
    dp = [[-1 for _ in range(m)] for _ in range(n)] # Initialize the DP table
    def helper(i: int, j: int) -> bool:
        if i < 0:
            return j < 0 or set(p[:j + 1]) == {'*'}
        if j < 0:
            return i < 0
        if dp[i][j] != -1: return dp[i][j]  # If the result was stored in DP table, return it
        
        if p[j] == '?' or s[i] == p[j]:
            dp[i][j] = helper(i - 1, j - 1)  # Store the result in DP table
            return dp[i][j]

        if p[j] == '*':
            dp[i][j] = helper(i - 1, j) or helper(i, j - 1)  # Store the result in DP table
            return dp[i][j]

        dp[i][j] = False    # Store the result in DP table
        return False

    return helper(n - 1, m - 1)

if __name__ == '__main__':

    testCases = [
        ("aa", "a"),    # false
        ("aa", '*'),    # true
        ("cb", '?a'),   # false
    ]

    for i, testCase in enumerate(testCases):
        s, p = testCase
        print(f'TestCase {i}: i/p: s={s}, p={p}; o/p: {isMatch(s, p)}')