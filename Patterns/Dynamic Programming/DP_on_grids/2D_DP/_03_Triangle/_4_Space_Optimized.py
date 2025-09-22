from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    rows = len(triangle)
    prevRow = triangle[-1]

    for row in range(rows - 2, -1, -1):
        for idx in range(row + 1):
            left = prevRow[idx] + triangle[row][idx]
            right = prevRow[idx + 1] + triangle[row][idx]
            prevRow[idx] = min(left, right)
    
    return prevRow[0]

if __name__ == '__main__':
    testCases = [
        [[2],[3,4],[6,5,7],[4,1,8,3]],  # 11
        [[-10]],                        # -10
    ]

    for i, triangle in enumerate(testCases):
        print(f'TestCase {i}: i/p: triangle = {triangle}; o/p: {minimumTotal(triangle)}')