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
    dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    # Base Case:
    # 1. Already handled i > j => 0
    # 2. i == j
    for i in range(n):
        dp[i][i][1] = 1 if expr[i] == 'T' else 0
        dp[i][i][0] = 1 if expr[i] == 'F' else 0

    # Start iterating over the changing parameters in Top-Down approach in reverse order and 
    # "f(i, j, k) => dp[i][j][k]"
    for i in range(n - 1, -1, -1):
        for j in range(i + 2, n):
            for wantTrue in range(2):            
                ways = 0
                for k in range(i + 1, j, 2):
                    lT = dp[i][k - 1][1]
                    lF = dp[i][k - 1][0]
                    rT = dp[k + 1][j][1]
                    rF = dp[k + 1][j][0]
                
                    if expr[k] == '&':
                        if wantTrue == 1: ways = (ways + (lT * rT) % mod) % mod
                        else: ways = (ways + (lF * rT) % mod + (lF * rF) % mod + (lT * rF) % mod) % mod
                    elif expr[k] == '|':
                        if wantTrue == 1: ways = (ways + (lT * rT) % mod + (lT * rF) % mod + (lF * rT) % mod) % mod
                        else: ways = (ways + (lF * rF) % mod) % mod
                    else:
                        if wantTrue == 1: ways = (ways + (lT * rF) % mod + (lF * rT) % mod) % mod
                        else: ways = (ways + (lT * rT) % mod + (lF * rF) % mod) % mod
                    
                dp[i][j][wantTrue] =  ways
    
    return dp[0][n - 1][1]

if __name__ == '__main__':
    testCases = [
        "T|T&F^T", # 4
        "T^F|F", # 2
        "T^F", # 1
    ]

    for i, expr in enumerate(testCases):
        print(f"TestCase {i}:- i/p: expr={expr}; o/p: {countTrue(expr)}")