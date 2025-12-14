# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

"""
    @question(LC 424):
        You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter you can get after performing the above operations.

    ----------------------------------------------------------------
    ----------------------------------------------------------------

        Example 1:
            Input: s = "ABAB", k = 2
            Output: 4
            Explanation: Replace the two 'A's with two 'B's or vice versa.

        ----------------------------------------------------------------

        Example 2:
            Input: s = "AABABBA", k = 1
            Output: 4
            Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
                The substring "BBBB" has the longest repeating letters, which is 4.
                There may exists other ways to achieve this answer too.
        
    ----------------------------------------------------------------
    ----------------------------------------------------------------
                
        Constraints:
            1 <= s.length <= 105
            s consists of only uppercase English letters.
            0 <= k <= s.length
"""

def charReplacement(s: str) -> int:
    n = len(s)
    l, r = 0, 0
    freq = [0] * 26
    maxLen = 0
    maxFreq = 0
    while r < n:
        freq[ord(s[r]) - ord('A')] += 1
        maxFreq = max(maxFreq, freq[ord(s[r]) - ord('A')])
        if r - l + 1 - maxFreq <= k:
            maxLen = max(maxLen, r - l + 1)
        # No need for shrinking while loop, just a single-shrink is enough
        else:
            freq[ord(s[l]) - ord('A')] -= 1
            l += 1
        r += 1
    
    return maxLen

if __name__ == '__main__':
    testCases = [
        ("ABAB", 2), # 4
        ("AABABBA", 1), # 4
    ]

    for i, testCase in enumerate(testCases):
        s, k = testCase
        print(f"TestCase {i}:- i/p: s={s}, k={k}; o/p: {charReplacement(s, k)}")