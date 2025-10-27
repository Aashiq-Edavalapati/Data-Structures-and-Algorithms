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
    def helper(i: int, j: int) -> bool:
        # Base Cases
        # 1: i < 0 => string is completely exhausted, so if it matched the pattern then there are 2 possibilites:
        #     i. Pattern also exhausted (j < 0) or
        #     ii. All the chars left in pattern must be *'s
        if i < 0:
            return j < 0 or set(p[:j + 1]) == {'*'}
        # 2: j < 0 => Pattern in completely exhausted, so if string matched the pattern then string should also have been exhausted
        if j < 0:
            return i < 0
        
        # If the current chars match or curr char in pattern is '?' => move both pointers one step ahead
        if p[j] == '?' or s[i] == p[j]:
            return helper(i - 1, j - 1)

        # If the curr pattern char is '*' => Either compare it with 0 chars in the string or compare with one char so it would keep on checking 0, 1, 2, 3, ... chars recursively!
        if p[j] == '*':
            return helper(i - 1, j) or helper(i, j - 1)

        # If it's none of the above cases, then it's false
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