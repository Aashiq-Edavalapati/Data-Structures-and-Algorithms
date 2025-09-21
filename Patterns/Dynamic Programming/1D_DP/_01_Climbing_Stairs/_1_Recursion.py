# Count => return 1 in all the valid base cases!

"""
    3 steps:
        1. Represent everything in terms of indices.
            0, 1, ...., n => Treat each number as an index
        2. Do all possible stuffs acc. to the problem statement.
            Jump 1 step or Jump 2 steps => f(n - 1) and f(n - 2)
        3. Count => Sum of all stuffs
            f(n - 1) + f(n - 2)
"""

def countWaysToClimb(n: int) -> int:
    if n == 0: return 1
    if n == 1: return 1

    return countWaysToClimb(n - 1) + countWaysToClimb(n - 2)

if __name__ == '__main__':
    testCases = list(range(46))
    for i, n in enumerate(testCases):
        print(f'TestCase {i}: i/p: {n} o/p:{countWaysToClimb(n)}')