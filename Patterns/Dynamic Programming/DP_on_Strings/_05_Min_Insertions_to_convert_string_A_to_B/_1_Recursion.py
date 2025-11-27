# Link: https://leetcode.com/problems/delete-operation-for-two-strings/

def lcs(str1: str, str2: str) -> int:
    n1, n2 = len(str1), len(str2)
    def solve(idx1: int, idx2: int) -> int:
        if idx1 < 0 or idx2 < 0: return 0 # If idx is out of bound in either of the string => We've reached to the end of one of the strings!

        # If the current character matches => Increase count and move both the pointers to next pos.
        if str1[idx1] == str2[idx2]:
            return 1 + solve(idx1 - 1, idx2 - 1)

        # If they don't match take max of moving only one pointer each time to next pos
        return max(solve(idx1 - 1, idx2), solve(idx1, idx2 - 1))
    
    return solve(n1 - 1, n2 - 1)

def minInsertionsOrDeletions(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    return n1 + n2 - 2 * lcs(s1, s2)

if __name__ == '__main__':
    testCases = [
        ("sea", "eat"),       # 2
        ("leetcode", "etco"), # 4 
    ]

    for i, testCase in enumerate(testCases):
        s1, s2 = testCase
        print(f"TestCase {i}: i/p: s1={s1}, s2={s2}; o/p: {minInsertionsOrDeletions(s1, s2)}")
    