# Link: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

# Patterns: Monotonic Stack

"""
    @question:
        Given a string s, return the of s that contains all the distinct characters of s exactly once.

    =====================================================================

        Example 1:
        Input: s =bc"

        ---------------------------------------------------------------------

        Example 2:
            Input: s = "cbacdcbc"
            Output: "acdb"

    =====================================================================

        Constraints:
            1 <= s.length <= 1000
            s consists of lowercase English letters.
"""

def smallestSubsequence(s: str) -> str:
    lastPos = {}
    for i, char in enumerate(s):
        lastPos[char] = i
    
    seq = []
    included = set()
    for i, char in enumerate(s):
        if char not in included:
            while seq and char < seq[-1] and lastPos[seq[-1]] > i:
                included.remove(seq.pop())

            seq.append(char)
            included.add(char)

    return ''.join(seq)

if __name__ == '__main__':
    testCases = [
        "bcabc", # abc
        "cbacdcbc", # acdb
    ]

    for i, events in enumerate(testCases):
        print(f"TestCase {i}:- i/p: events={events}; o/p: {maxTwoEvents(events)}")