# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
    @question:
        Given a string s, find the length of the longest substring without duplicate characters.

    -------------------------------------------------------------------
    -------------------------------------------------------------------        

        Example 1:
            Input: s = "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

        -------------------------------------------------------------------

        Example 2:
            Input: s = "bbbbb"
            Output: 1
            Explanation: The answer is "b", with the length of 1.

        -------------------------------------------------------------------

        Example 3:
            Input: s = "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3.
                Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        
    -------------------------------------------------------------------
    -------------------------------------------------------------------

        Constraints:
            0 <= s.length <= 5 * 104
            s consists of English letters, digits, symbols and spaces.
"""

def longestSubstrLen(s):
    n = len(s)
    l, r, maxLen = 0, 0, 0
    chars = {}
    while r < n:
        char = s[r]
        if char in chars and chars[char] >= l:
            l = chars[char] + 1
        chars[char] = r
        r += 1
        maxLen = max(r - l, maxLen)
    
    return maxLen

if __name__ == '__main__':
    testCases = [
        "abcabcbb", # 3
        "bbbbb", # 1
        "pwwkew", # 3
        "", # 0
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {longestSubstrLen(s)}")