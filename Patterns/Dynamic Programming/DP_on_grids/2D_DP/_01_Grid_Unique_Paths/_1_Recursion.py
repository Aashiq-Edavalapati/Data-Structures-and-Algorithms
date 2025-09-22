def countPaths(row: int, col: int) -> int:
    """
    
    """
    # --- Base Cases ---
    if row == 0 and col == 0:
        return 1
    if row < 0 or col < 0:
        return 0
    # --- ---

    up = countPaths(row - 1, col)
    left = countPaths(row, col - 1)

    return left + up

if __name__ == '__main__':
    testCases = [
        (2, 2),
        (3, 4)
    ]

    for i, inp in enumerate(testCases):
        m, n = inp
        print(f'TestCase {i}:-  i/p: m: {m}, n: {n}; o/p: {countPaths(m - 1, n - 1)}')