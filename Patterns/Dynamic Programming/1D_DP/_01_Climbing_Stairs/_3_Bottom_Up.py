# if n == 0: return 1
# if n == 1: return 1
# return countWaysToClimb(n - 1) + countWaysToClimb(n - 2)

def countWaysToClimb(n: int) -> int:
    if n < 2: return n
    dp = [0] * (n + 1)
    dp[0] = 1 # Base Case
    dp[1] = 1 # Base Case
    for i in range(2, n + 1):
        # Replace f(n) with dp[n] in the recurrence relation
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] # Required answer f(n) => dp[n]

if __name__ == '__main__':
    testCases = list(range(46))
    for i, n in enumerate(testCases):
        print(f'TestCase {i}: i/p: {n} o/p:{countWaysToClimb(n)}')