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

def lcs(str1: str, str2: str) -> int:
    n1, n2 = len(str1), len(str2)
    def solve(idx1: int, idx2: int) -> int:
        if idx1 < 0 or idx2 < 0: return 0 # If idx is out of bound in either of the string => We've reached to the end of one of the strings!

        # If the current character matches => Increase count and move both the pointers to next pos.
        if str1[idx1] == str2[idx2]:
            return 1 + solve(idx1 - 1, idx2 - 1)

        # If they don't match take max of moving only one pointer each time to next pos
        return max(solve(idx1 - 1, idx2), solve(idx1, idx2 - 1))
    
    return solve(n1 - 1, n2 - 1)

if __name__ == '__main__':
    testCases = [
        ("abcde", "ace"),   # 3
        ("abc", "abc"),     # 3
        ("abc", "def"),     # 0
        ("oxcpqrsvwf", "shmtulqrypy"), # 2
    ]

    for i, inp in enumerate(testCases):
        str1, str2 = inp
        print(f'TestCase{i}: i/p: str1={str1}, str2={str2}; o/p: {lcs(str1, str2)}')