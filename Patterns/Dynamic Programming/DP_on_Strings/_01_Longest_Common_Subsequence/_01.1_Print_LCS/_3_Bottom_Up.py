# Link: https://leetcode.com/problems/longest-common-subsequence/

"""
    @question:
        Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

        For example, "ace" is a subsequence of "abcde".
        A common subsequence of two strings is a subsequence that is common to both strings.
        
        Example 1:
            Input: text1 = "abcde", text2 = "ace" 
            Output: 3  
            Explanation: The longest common subsequence is "ace" and its length is 3.
        ------------------------------------------------------------------------------
        Example 2:
            Input: text1 = "abc", text2 = "abc"
            Output: 3
            Explanation: The longest common subsequence is "abc" and its length is 3.
        ------------------------------------------------------------------------------
        Example 3:
            Input: text1 = "abc", text2 = "def"
            Output: 0
            Explanation: There is no such common subsequence, so the result is 0.
    -----------------------------------------------------------------------------------

        Constraints:
            1 <= text1.length, text2.length <= 1000
            text1 and text2 consist of only lowercase English characters.
"""

def printLCS(str1: str, str2: str) -> int:
    n1, n2 = len(str1), len(str2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)] # Initialize DP table

    # Start iterating
    for idx1 in range(1, n1 + 1): # Start from 1 to prevent index out of bound
        for idx2 in range(1, n2 + 1): # Start from 1 to prevent index out of bound
            if str1[idx1 - 1] == str2[idx2 - 1]: 
                dp[idx1][idx2] = 1 + dp[idx1 - 1][idx2 - 1] # 1 + f(idx1 - 1, idx2 - 1) => 1 + dp[idx1 - 1][idx2 - 1]
            else:
                dp[idx1][idx2] = max(dp[idx1 - 1][idx2], dp[idx1][idx2 - 1])
    lcs = [""] * dp[n1][n2]
    pos = dp[n1][n2] - 1
    i, j = n1, n2
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[pos] = str1[i - 1]
            pos -= 1
            if pos == -1:
                break
            i -= 1
            j -= 1
        
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
        
    return "".join(lcs)

if __name__ == '__main__':
    testCases = [
        ("abcde", "ace"),   # 3
        ("abc", "abc"),     # 3
        ("abc", "def"),     # 0
        ("oxcpqrsvwf", "shmtulqrypy"), # 2
    ]

    for i, inp in enumerate(testCases):
        str1, str2 = inp
        print(f'TestCase{i}: i/p: str1={str1}, str2={str2}; o/p: {printLCS(str1, str2)}')