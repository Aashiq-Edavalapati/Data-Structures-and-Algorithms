# Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

"""
    @question(LC 1358):
        Given a string s consisting only of characters a, b and c.

        Return the number of substrings containing at least one occurrence of all these characters a, b and c.

    --------------------------------------------------------------------
    --------------------------------------------------------------------

        Example 1:
            Input: s = "abcabc"
            Output: 10
            Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

        --------------------------------------------------------------------

        Example 2:
            Input: s = "aaacb"
            Output: 3
            Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

        --------------------------------------------------------------------

        Example 3:
            Input: s = "abc"
            Output: 1
        
    --------------------------------------------------------------------
    --------------------------------------------------------------------

        Constraints:
            3 <= s.length <= 5 x 10^4
            s only consists of a, b or c characters.
"""

"""
    @intuition:
        Once we find a minimum valid window, then it's like all the chars before the min window can also be added to the curr substring.

        This is the most optimal => Single pass
"""
def noOfSubstrings(s: str) -> int:
    n = len(s)
    lastSeen = [-1] * 3
    cnt = 0
    for i in range(n):
        lastSeen[ord(s[i]) - ord('a')] = i
        cnt += 1 + min(lastSeen)

    return cnt

"""
    @intuition:
        Each time when we found a valid window(need not be min) ending at an index, then all chars after it can also be added to make a valid substring.

        Ex: aabcabc
                In this, we first find a valid substring at c(index = 3), but the min window is abc, not aabc, so we are missing out the substrings starting with 2nd a, that's why we try to shrink the window until it becomes invalid and keep updating the count.
        
        This is still optimal, but a bit naive and direct compared to the above approach!
"""
def noOfSubstrings2(s: str) -> int:
    n = len(s)
    a, b, c = 0, 0, 0
    cnt = 0
    l, r = 0, 0
    while r < n:
        while r < n and (a == 0 or b == 0 or c == 0):
            if s[r] == 'a': a += 1
            elif s[r] == 'b': b += 1
            else: c += 1
            r += 1
        
        if a > 0 and b > 0 and c > 0: cnt += n - r + 1

        while a > 0 and b > 0 and c > 0:
            if s[l] == 'a': a -= 1
            elif s[l] == 'b': b -= 1
            else: c -= 1
            l += 1
            if a > 0 and b > 0 and c > 0: cnt += n - r + 1

    return cnt

if __name__ == '__main__':
    testCases = [
        "abcabc", # 10
        "aaacb", # 3
        "abc", # 1
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {noOfSubstrings(s)}")