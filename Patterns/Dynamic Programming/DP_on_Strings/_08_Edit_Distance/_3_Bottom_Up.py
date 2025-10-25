# Link: https://leetcode.com/problems/edit-distance/description/

"""
    @question:
        Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

        You have the following three operations permitted on a word:

        Insert a character
        Delete a character
        Replace a character
        
------------------------------------------------------------
        Example 1:
            Input: word1 = "horse", word2 = "ros"
            Output: 3
            Explanation: 
                horse -> rorse (replace 'h' with 'r')
                rorse -> rose (remove 'r')
                rose -> ros (remove 'e')
        ----------------------------------------------------
        Example 2:
            Input: word1 = "intention", word2 = "execution"
            Output: 5
            Explanation: 
                intention -> inention (remove 't')
                inention -> enention (replace 'i' with 'e')
                enention -> exention (replace 'n' with 'x')
                exention -> exection (replace 'n' with 'c')
                exection -> execution (insert 'u')
-------------------------------------------------------------------------------
        Constraints:
            0 <= word1.length, word2.length <= 500
            word1 and word2 consist of lowercase English letters.
"""

def editDistance(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)] # Initialize DP Table Add an extra row and col to handle negative index base cases

    # Base Cases
    # 1: j < 0
    for i in range(n1 + 1):
        dp[i][0] = i
    # 2: i < 0
    for j in range(n2 + 1):
        dp[0][j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                continue
            
            insert = 1 + dp[i][j - 1]
            delete = 1 + dp[i - 1][j]
            replace = 1 + dp[i - 1][j - 1]

            dp[i][j] = min(insert, delete, replace) # Store the result in the DP table
    
    return dp[n1][n2]

if __name__ == '__main__':
    testCases = [
        ("horse", "ros"),   # 3
        ("intention", "execution"), # 5
        ("", "abc"),    # 3
        ("abc", ""),    # 3
    ]

    for i, testCase in enumerate(testCases):
        s1, s2 = testCase
        print(f"TestCase {i}: i/p: s1={s1}, s2={s2}; o/p: {editDistance(s1, s2)}")