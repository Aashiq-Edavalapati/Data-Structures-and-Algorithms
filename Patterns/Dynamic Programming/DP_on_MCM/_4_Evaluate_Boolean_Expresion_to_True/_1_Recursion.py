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

"""
    @intuition:
        Since we are trying is out all possible partitions of the expression => Clear hint that we should use partition DP

        We have 3 operators (&, |, ^). For each partition we have to count no. of ways we can make the whole expression True.
        So, we need to think how to count this:
            After each partition, let's say lT, lF, rT, rF be no. of ways in which left expr. can be True, False, right expr. can be True, False respectively.
            1. IF operator is '&':
                # T & T = T
                No. ways for the whole expression to be True = lT * rT
                # T & F = F, F & T = F, F & F = F
                No. ways for the exprr. to be False = lT * rF + lF * rT + lF * rF
            
            2. IF operator is '|':
                # T | T = T, T | F = T, F | T = T
                ways for true = lT * rT + lT * rF + lF * rT
                # F | F = F
                ways for false = lF * rF
            
            3. IF operator is '^':
                # T ^ F = T, F ^ T = T
                ways for true = lT * rF + lF * rT
                # T ^ T = F, F ^ F = F
                ways for false = lT * rT + lF * rF
"""
def countTrue(expr: str) -> int:
    n = len(expr)
    mod = 10 ** 9 + 7
    def helper(i: int, j: int, wantTrue: int) -> int:
        # Base Cases
        # 1. Whole exprr. has been exhausted
        if i > j: return 0
        # 2. i == j => No more partitions => return count of False or True as requested
        if i == j:
            if wantTrue == 1:
                return 1 if expr[i] == 'T' else 0
            else:
                return 1 if expr[i] == 'F' else 0
        
        ways = 0
        # Start from next symbol(i.e., operator and try partitioning at all the operators in the range)
        for k in range(i + 1, j, 2):
            lT = helper(i, k - 1, 1) # No. ways for left partition to be true
            lF = helper(i, k - 1, 0) # No. ways for left partition to be false
            rT = helper(k + 1, j, 1) # No. ways for right partition to be true
            rF = helper(k + 1, j, 0) # No. ways for right partition to be false
        
            if expr[k] == '&':
                if wantTrue == 1: ways = (ways + (lT * rT) % mod) % mod
                else: ways = (ways + (lF * rT) % mod + (lF * rF) % mod + (lT * rF) % mod) % mod
            elif expr[k] == '|':
                if wantTrue == 1: ways = (ways + (lT * rT) % mod + (lT * rF) % mod + (lF * rT) % mod) % mod
                else: ways = (ways + (lF * rF) % mod) % mod
            else:
                if wantTrue == 1: ways = (ways + (lT * rF) % mod + (lF * rT) % mod) % mod
                else: ways = (ways + (lT * rT) % mod + (lF * rF) % mod) % mod
            
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