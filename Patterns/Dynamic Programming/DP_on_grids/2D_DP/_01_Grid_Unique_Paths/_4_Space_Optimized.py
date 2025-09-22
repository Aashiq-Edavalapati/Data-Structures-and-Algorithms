def countPaths(m: int, n: int) -> int:
    """
    """
    prevCol = 1
    prevRow = [0] * n
    prevRow[0] = 1
    for row in range(m):
        for col in range(n):
            if row == 0 and col == 0: continue
            left, up = 0, 0
            if col > 0: left = prevCol
            if row > 0: up = prevRow[col]
            
            prevCol = left + up
            prevRow[col] = prevCol
    
    return prevCol

if __name__ == '__main__':
    testCases = [
        (2, 2),
        (3, 4)
    ]

    for i, inp in enumerate(testCases):
        m, n = inp
        print(f'TestCase {i}:-  i/p: m: {m}, n: {n}; o/p: {countPaths(m, n)}')