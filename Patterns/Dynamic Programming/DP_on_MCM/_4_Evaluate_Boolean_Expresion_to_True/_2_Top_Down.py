"""
    @question:
        You are given a string expr consisting of the characters

            'T' — represents true
            'F' — represents false
            '&' — the logical AND operator
            '|' — the logical OR operator
            '^' — the logical XOR (exclusive-or) operator

        expr is guaranteed to follow the pattern operand operator operand operator … operand (i.e. it always starts and ends with an operand and no two operators are adjacent).

        Return the number of distinct ways to fully parenthesize expr such that the whole expression evaluates to true.

        Because the answer can be very large, return it modulo 1e9+7.

    ----------------------------------------------------------------------------------------
    ----------------------------------------------------------------------------------------
        
        Examples:
            Input: expr = "T|T&F^T"
            Output: 4
            Explanation:
            The expression can be parenthesized as follows (✓ marks variants that evaluate to true):
                1. ((T|T)&(F^T)) ✓
                2. (T|(T&(F^T))) ✓
                3. (((T|T)&F)^T) ✓
                4. (T|((T&F)^T)) ✓
                5. ((T|(T&F))^T)   → false
                6. (T|T)&F^T     → false

            Therefore 4 distinct parenthesizations evaluate to true.

        --------------------------------------------------------------------------------------
        
            Input: expr = "T^F|F"
            Output: 2
            Explanation:
                Two parenthesizations evaluate to true:
                    • ((T ^ F) | F)
                    • (T ^ (F | F))
        
        ----------------------------------------------------------------------------------------
        ----------------------------------------------------------------------------------------

        Constraints:
            1 <= expr.length <= 100
            expr[i] is 'T', 'F', '&', '|', or '^'.
            Operands ('T' or 'F') and operators alternate, so expr always has odd length.
            The answer fits in a signed 32-bit integer.
"""

def countTrue(expr: str) -> int:
    n = len(expr)
    mod = 10 ** 9 + 7
    # Initialize DP Table
    dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    def helper(i: int, j: int, wantTrue: int) -> int:
        if i > j: return 0
        if i == j:
            if wantTrue == 1:
                return 1 if expr[i] == 'T' else 0
            else:
                return 1 if expr[i] == 'F' else 0
        if dp[i][j][wantTrue] != -1: return dp[i][j][wantTrue] # If result was stored in DP table, return it
        
        ways = 0
        for k in range(i + 1, j, 2):
            lT = helper(i, k - 1, 1)
            lF = helper(i, k - 1, 0)
            rT = helper(k + 1, j, 1)
            rF = helper(k + 1, j, 0)
        
            if expr[k] == '&':
                if wantTrue == 1: ways = (ways + (lT * rT) % mod) % mod
                else: ways = (ways + (lF * rT) % mod + (lF * rF) % mod + (lT * rF) % mod) % mod
            elif expr[k] == '|':
                if wantTrue == 1: ways = (ways + (lT * rT) % mod + (lT * rF) % mod + (lF * rT) % mod) % mod
                else: ways = (ways + (lF * rF) % mod) % mod
            else:
                if wantTrue == 1: ways = (ways + (lT * rF) % mod + (lF * rT) % mod) % mod
                else: ways = (ways + (lT * rT) % mod + (lF * rF) % mod) % mod
        
        # Store the result in DP Table
        dp[i][j][wantTrue] = ways
        return ways
    
    return helper(0, n - 1, 1)

if __name__ == '__main__':
    testCases = [
        "T|T&F^T", # 4
        "T^F|F", # 2
        "T^F", # 1
    ]

    for i, expr in enumerate(testCases):
        print(f"TestCase {i}:- i/p: expr={expr}; o/p: {countTrue(expr)}")