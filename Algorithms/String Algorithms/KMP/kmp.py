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

        # Store the starting index of every occurrence of the pattern.
        found = []

        while i < n:
            if text[i] == pattern[j]:
                # Characters match, so move forward in both strings.
                i += 1
                j += 1

                if j == m:
                    # We matched the entire pattern!
                    # `i` is currently just after the match,
                    # so the starting index is `i - j`.
                    found.append(i - j)

                    # The pattern may overlap with itself.
                    # Instead of starting from scratch, use LPS
                    # to keep the longest valid prefix we've already matched.
                    j = lps[j - 1]

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

        return found



if __name__ == '__main__':
    test_cases = [
        ("ABABDABABABABCABAB", "ABAB"),
        ("AAAAA", "AAA"),
        ("ABCABCABC", "ABC"),
        ("HELLO WORLD", "WORLD"),
        ("ABCDEFG", "XYZ"),
    ]

    kmp = KMP()

    for case_no, (text, pattern) in enumerate(test_cases, 1):
        result = kmp.search(pattern, text)

        print(f"Test Case {case_no}:")
        print(f"  Text    = {text}")
        print(f"  Pattern = {pattern}")
        print(f"  Output  = {result}")
        print("-" * 40)