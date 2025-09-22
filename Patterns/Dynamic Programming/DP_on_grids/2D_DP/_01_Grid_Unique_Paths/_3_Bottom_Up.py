def countPaths(m: int, n: int) -> int:
    """
    """
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    for row in range(m):
        for col in range(n):
            if row == 0 and col == 0: continue
            if col > 0:
                left = dp[row][col - 1]
            else:
                left = 0
            if row > 0:
                up = dp[row - 1][col]
            else:
                up = 0
            
            dp[row][col] = left + up
    
    return dp[m - 1][n - 1]

if __name__ == '__main__':
    testCases = [
        (2, 2),
        (3, 4)
    ]

    for i, inp in enumerate(testCases):
        m, n = inp
        print(f'TestCase {i}:-  i/p: m: {m}, n: {n}; o/p: {countPaths(m, n)}')