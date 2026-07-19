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
    # Store the last occurrence of every character
    lastPos = {}
    for i, char in enumerate(s):
        lastPos[char] = i

    stack = []
    included = set()

    for i, char in enumerate(s):
        # Skip duplicate characters
        if char in included:
            continue

        # Remove larger characters if they appear again later
        while (
            stack
            and char < stack[-1]
            and lastPos[stack[-1]] > i
        ):
            included.remove(stack.pop())

        stack.append(char)
        included.add(char)

    return "".join(stack)

if __name__ == '__main__':
    testCases = [
        "bcabc", # abc
        "cbacdcbc", # acdb
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {smallestSubsequence(s)}")