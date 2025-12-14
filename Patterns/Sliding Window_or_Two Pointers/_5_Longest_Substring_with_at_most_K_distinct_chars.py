"""
    @question:
        Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.

    --------------------------------------------------------------------
    --------------------------------------------------------------------
        
        Example 1
            Input : s = "aababbcaacc" , k = 2
            Output : 6
            Explanation : The longest substring with at most two distinct characters is "aababb".
                The length of the string 6.

        --------------------------------------------------------------------

        Example 2
            Input : s = "abcddefg" , k = 3
            Output : 4
            Explanation : The longest substring with at most three distinct characters is "bcdd".
                The length of the string 4.
    
    --------------------------------------------------------------------
    --------------------------------------------------------------------

        Constraints

            1 <= s.length <= 105
            1 <= k <= 26
"""
def kDistChars(s: str, k: int) -> int:
    n = len(s)
    l, r, maxLen = 0, 0, 0
    chars = {}
    while r < n:
        char = s[r]
        chars[char] = chars.get(char, 0) + 1
        
        # Note that we can eliminate the while loop because any way we have to move the right pointer atleast the same number or times we move left pointer if this is a while loop instead of if, so it doesn't really matter if we shrink the window and make it valid if it doesn't actually exceed the maxLen. It will eventually fix itself
        if len(chars) > k:
            char = s[l]
            chars[char] -= 1
            l += 1
            if chars[char] == 0:
                del chars[char]

        maxLen = max(maxLen, r - l + 1)
        r += 1

    return maxLen

if __name__ == '__main__':
    testCases = [
        ("aababbcaacc", 2), # 6
        ("abcddefg", 3), # 4
        ("abccab", 4), # 6
        ("aabcbc", 2), # 4
        ("aabccc", 2), # 5
        ("abcbbbbcccbddd", 2), # 10
    ]

    for i, testCase in enumerate(testCases):
        s, k = testCase
        print(f"TestCase {i}:- i/p: s={s}, k={k}; o/p: {kDistChars(s, k)}")