def countPaths(m: int, n: int) -> int:
    """
    """
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    def helper(row: int, col: int) -> int:
        # --- Base Cases ---
        if row == 0 and col == 0:
            return 1
        if row < 0 or col < 0:
            return 0
        # --- ---
        if dp[row][col] != -1: return dp[row][col]

        up = helper(row - 1, col)
        left = helper(row, col - 1)

        dp[row][col] = left + up
        return dp[row][col]
    
    return helper(m - 1, n- 1)

if __name__ == '__main__':
    testCases = [
        (2, 2),
        (3, 4)
    ]

    for i, inp in enumerate(testCases):
        m, n = inp
        print(f'TestCase {i}:-  i/p: m: {m}, n: {n}; o/p: {countPaths(m, n)}')