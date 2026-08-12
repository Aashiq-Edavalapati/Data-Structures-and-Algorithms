# Link: https://leetcode.com/problems/rotate-string/

from typing import List

class KMP:
    def computeLPS(self, pattern: str) -> List[int]:
        m = len(pattern)
        lps = [0] * m

        # `length` tells us how many characters of the prefix currently match the suffix ending at `i - 1`.
        #
        # We start `i` from 1 because lps[0] is always 0:
        #   a single character cannot have a proper prefix.
        i, length = 1, 0

        while i < m:
            if pattern[i] == pattern[length]:
                # We found one more matching character between the prefix and suffix.
                length += 1
                lps[i] = length
                i += 1

            elif length != 0:
                # The current prefix/suffix match failed.
                #
                # Instead of starting from length = 0, try the next longest prefix that we already know can be useful.
                # This is the main idea behind KMP.
                length = lps[length - 1]

            else:
                # There is no smaller prefix we can fall back to,
                # so this position has no matching prefix/suffix.
                lps[i] = 0
                i += 1

        return lps

    def search(self, pattern: str, text: str) -> List[int]:
        # Build the LPS array once for the pattern.
        # It tells us how far we can "fall back" whenever a mismatch occurs.
        lps = self.computeLPS(pattern)

        m, n = len(pattern), len(text)

        # `i` -> current position in the text
        # `j` -> current position in the pattern
        i, j = 0, 0

        while i < n:
            if text[i] == pattern[j]:
                # Characters match, so move forward in both strings.
                i += 1
                j += 1

                if j == m:
                    # We matched the entire pattern!
                    # `i` is currently just after the match,
                    # so the starting index is `i - j`.
                    return True

            elif j != 0:
                # Mismatch after matching some part of the pattern.
                #
                # Don't move `i` backwards and don't restart from j = 0.
                # Use the LPS array to reuse the part of the pattern
                # that we already know matches.
                j = lps[j - 1]

            else:
                # Mismatch happened at the very first pattern character.
                # There is nothing to fall back to, so simply move
                # to the next character in the text.
                i += 1

        return False

class Solution:
    def rotateString(s: str, goal: str) -> bool:
        m, n = len(goal), len(s)
        if m != n: return False
        s += s
        n += n
        kmp = KMP()
        return kmp.search(s, goal)

if __name__ == '__main__':
    testCases = [
        ("abc", "ab"), # False
        ("c", "w"), # False
        ("abcde", "cdeab"), # True
        ("abcde", "abced"), # False
    ]

    for i, (s, goal) in enumerate(testCases):
        sol = Solution()
        print(f"Testcase {i}:- i/p: s={s}, goal={goal}; o/p: {sol.rotateString(s, goal)}")