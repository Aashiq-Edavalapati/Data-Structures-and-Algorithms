# Link: https://leetcode.com/problems/minimum-window-substring/

"""
    @question(LC 76):
        Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

        The testcases will be generated such that the answer is unique.

    =================================================================
    =================================================================

        Example 1:
            Input: s = "ADOBECODEBANC", t = "ABC"
            Output: "BANC"
            Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

        =================================================================
            
        Example 2:
            Input: s = "a", t = "a"
            Output: "a"
            Explanation: The entire string s is the minimum window.

        =================================================================
        
        Example 3:
            Input: s = "a", t = "aa"
            Output: ""
            Explanation: Both 'a's from t must be included in the window.
                Since the largest window of s only has one 'a', return empty string.
        
    =================================================================
    =================================================================

        Constraints:
            m == s.length
            n == t.length
            1 <= m, n <= 105
            s and t consist of uppercase and lowercase English letters.
"""
from collections import defaultdict

"""
    Instead of scanning through frequencies of each character in t by iterating over t everytime, we can optimize it by increasing the freq when shrinking the window and decreasing the freq when expanding the window. And keep track of all the chars availability using a cnt var and comparing it with length of t.
"""
def minWindow(s: str, t: str) -> str:
    if not s or not t: return ""
    n, m = len(s), len(t)
    if m > n: return ""

    freq = defaultdict(int)
    for char in t:
        freq[char] += 1
    
    l, r = 0, 0
    minLen = n + 1
    startInd = -1
    cnt = 0
    while r < n:
        if freq[s[r]] > 0: cnt += 1
        freq[s[r]] -= 1
        while cnt == m:
            if r - l + 1 < minLen:
                minLen = r - l + 1
                startInd = l
            freq[s[l]] += 1
            if freq[s[l]] > 0: cnt -= 1
            l += 1
        
        r += 1
        
    return s[startInd:startInd + minLen] if startInd != -1 else ""

if __name__ == '__main__':
    testCases = [
        ("ADOBECODEBANC", "ABC"), # BANC
        ("ADOBECODEBANC", ""), # ""
        ("a", "a"), # a
        ("a", "aa"), # ""
        ("ab", "a"), # "a"
    ]

    for i, testCase in enumerate(testCases):
        s, t = testCase
        print(f"TestCase {i}:- i/p: s={s}, t={t}; o/p: {minWindow(s, t)}")