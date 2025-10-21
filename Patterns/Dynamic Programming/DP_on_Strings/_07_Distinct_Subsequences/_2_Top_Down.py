# Link: https://leetcode.com/problems/distinct-subsequences/

def numDistinct(s: str, t: str) -> int:
    n1, n2 = len(s), len(t)
    dp = [[-1 for _ in range(n2)] for _ in range(n1)] # Initialize DP Table
    def helper(i: int, j: int) -> int:
        # Base Cases
        if i < 0:
            return 0
        # If result was already stored in DP table => return the res
        if dp[i][j] != -1:
            return dp[i][j]
        if j == 0:
            # Store the result in DP Table
            dp[i][0] = 1 + helper(i - 1, j) if s[i] == t[0] else helper(i - 1, j)
            return dp[i][0]
        
        pick = 0
        if s[i] == t[j]:
            pick = helper(i - 1, j - 1)
        notPick = helper(i - 1, j)

        # Store the result in DP table
        dp[i][j] = pick + notPick
        return dp[i][j]
    
    return helper(n1 - 1, n2 - 1)

if __name__ == '__main__':
    testCases = [
        ("rabbbit", "rabbit"),  # 3
        ("babgbag", "bag"),     # 5
    ]

    for i, testCase in enumerate(testCases):
        s, t = testCase
        print(f'TestCase {i}: i/p: s={s}, t={t}; o/p: {numDistinct(s, t)}')