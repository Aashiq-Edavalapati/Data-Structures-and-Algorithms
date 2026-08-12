from typing import List


class RabinKarp:

    def search(self, pattern: str, text: str) -> List[int]:
        m, n = len(pattern), len(text)
        found = []

        # Pattern cannot fit inside the text.
        if m > n:
            return found

        # Base used for calculating the rolling hash.
        # 256 covers the standard ASCII character range.
        base = 256

        # A large prime number used to keep the hash values manageable
        # and reduce the chance of different strings having the same hash.
        mod = 10**9 + 7

        # `high` represents base^(m - 1) % mod.
        #
        # We'll use it later to remove the leftmost character
        # when the sliding window moves one position to the right.
        high = pow(base, m - 1, mod)

        pattern_hash = 0
        window_hash = 0

        # Calculate the initial hash of:
        # 1. The pattern
        # 2. The first window of the text having the same length
        #
        # Example:
        # pattern = "ABC"
        # window  = "ABC"
        for i in range(m):
            pattern_hash = (
                (pattern_hash * base) + ord(pattern[i])
            ) % mod

            window_hash = (
                (window_hash * base) + ord(text[i])
            ) % mod

        # Slide the window across the text.
        for i in range(n - m + 1):

            # Hashes matching does NOT guarantee that the strings
            # are actually equal because two different strings can
            # theoretically have the same hash.
            #
            # So we verify the actual substring whenever the hashes match.
            if pattern_hash == window_hash:
                if text[i:i + m] == pattern:
                    found.append(i)

            # Move the window one position to the right.
            if i < n - m:
                # Remove the contribution of the leftmost character.
                window_hash = (
                    window_hash
                    - ord(text[i]) * high
                ) % mod

                # Shift everything left in the hash and
                # add the new character entering the window.
                window_hash = (
                    window_hash * base
                    + ord(text[i + m])
                ) % mod

        return found


# ---------------- Driver Code ----------------

test_cases = [
    ("ABABDABABABABCABAB", "ABAB"),
    ("AAAAA", "AAA"),
    ("ABCABCABC", "ABC"),
    ("HELLO WORLD", "WORLD"),
    ("ABCDEFG", "XYZ"),
    ("ABABABAB", "ABAB"),
]

rabin_karp = RabinKarp()

for case_no, (text, pattern) in enumerate(test_cases, 1):
    result = rabin_karp.search(pattern, text)

    print(f"Test Case {case_no}:")
    print(f"  Text    = {text}")
    print(f"  Pattern = {pattern}")
    print(f"  Output  = {result}")
    print("-" * 40)