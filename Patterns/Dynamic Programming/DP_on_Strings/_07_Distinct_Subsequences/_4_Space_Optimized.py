# Link: https://leetcode.com/problems/distinct-subsequences/

def numDistinct(s: str, t: str) -> int:
    n1, n2 = len(s), len(t)
    prev = [0 for _ in range(n2)] # Initialize prev row
    # Base Case
    if s[0] == t[0]:
        prev[0] = 1

    for i in range(1, n1):
        # Base Case
        curr = [0 for _ in range(n2)]
        if s[i] == t[0]:
            curr[0] = 1 + prev[0] # dp[i][0] => curr[0] and dp[i - 1][0] => prev[0]
        else:
            curr[0] = prev[0] # dp[i][0] => curr[0] and dp[i - 1][0] => prev[0]
        
        for j in range(1, n2):
            pick = 0
            if s[i] == t[j]:
                pick = prev[j - 1] # dp[i - 1] => prev
            notPick = prev[j] # dp[i - 1] => prev

            curr[j] = pick + notPick # # dp[i] => curr
        prev = curr # Change the curr row as prev for next iteration
        
    return prev[n2 - 1]

if __name__ == '__main__':
    testCases = [
        ("rabbbit", "rabbit"),  # 3
        ("babgbag", "bag"),     # 5
    ]

    for i, testCase in enumerate(testCases):
        s, t = testCase
        print(f'TestCase {i}: i/p: s={s}, t={t}; o/p: {numDistinct(s, t)}')