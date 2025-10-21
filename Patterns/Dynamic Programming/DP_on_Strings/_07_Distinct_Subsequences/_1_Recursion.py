# Link: https://leetcode.com/problems/distinct-subsequences/

def numDistinct(s: str, t: str) -> int:
    n1, n2 = len(s), len(t)
    def helper(i: int, j: int) -> int:
        # Base Cases
        # 1. If i goes out of bound, then curr path is not valid => Return 0
        if i < 0: 
            return 0
        # 2. If j == 0 => all the chars from the 2nd char matched in t with s => 
        #      If s[i] == t[0] => A valid sequence found: 
        #           return 1 + f(i - 1, j) # pick = 1 + Not Pick = f(i - 1, j)
        #       else:
        #           return 0 + f(i - 1, j) # pick = 0 + Not Pick = f(i - 1, j)
        if j == 0:
            return 1 + helper(i - 1, j) if s[i] == t[0] else helper(i - 1, j)
        
        # Case 1: Pick the curr char in s if s[i] == t[j]
        pick = 0
        if s[i] == t[j]:
            pick = helper(i - 1, j - 1)
        # Case 2: Don't pick the curr char in s
        notPick = helper(i - 1, j)

        # Return all the valid combos
        return pick + notPick
    
    return helper(n1 - 1, n2 - 1)

if __name__ == '__main__':
    testCases = [
        ("rabbbit", "rabbit"),  # 3
        ("babgbag", "bag"),     # 5
    ]

    for i, testCase in enumerate(testCases):
        s, t = testCase
        print(f'TestCase {i}: i/p: s={s}, t={t}; o/p: {numDistinct(s, t)}')