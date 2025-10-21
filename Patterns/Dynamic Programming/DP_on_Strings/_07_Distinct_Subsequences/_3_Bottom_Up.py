# Link: https://leetcode.com/problems/distinct-subsequences/

def numDistinct(s: str, t: str) -> int:
    n1, n2 = len(s), len(t)
    dp = [[0 for _ in range(n2)] for _ in range(n1)] # Initialize DP table
    # Base Cases (2nd base case)
    if s[0] == t[0]:
        dp[0][0] = 1
    for i in range(1, n1):
        if s[i] == t[0]:
            dp[i][0] = 1 + dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][0]
    # Since, i < 0 is not a valid index, and any way we are going to get 0 as res for i < 0, the whole dp[0] will be 0's => We'll start iterating from i = 1

    # Start iterating over all the possible values
    for i in range(1, n1):
        for j in range(1, n2): # j = 0 is base case => Start from j = 1
            pick = 0
            if s[i] == t[j]:
                pick = dp[i - 1][j - 1] # f(i - 1, j - 1) => dp[i - 1][j - 1]
            notPick = dp[i - 1][j] # f(i -1 , j) => dp[i - 1][j]

            dp[i][j] = pick + notPick # f(i, j) => dp[i][j]
    
    return dp[n1 - 1][n2 - 1] # f(n1 - 1, n2 - 1) => dp[n1 - 1][n2 - 1]

if __name__ == '__main__':
    testCases = [
        ("rabbbit", "rabbit"),  # 3
        ("babgbag", "bag"),     # 5
    ]

    for i, testCase in enumerate(testCases):
        s, t = testCase
        print(f'TestCase {i}: i/p: s={s}, t={t}; o/p: {numDistinct(s, t)}')