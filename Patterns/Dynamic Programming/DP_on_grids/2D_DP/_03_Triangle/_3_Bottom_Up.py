from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    rows = len(triangle)
    dp = [[0 for _ in range(rows)] for _ in range(rows)]
    dp[-1] = triangle[-1]
    for row in range(rows - 2, -1, -1):
        for idx in range(row + 1):
            left = dp[row + 1][idx] + triangle[row][idx]
            right = dp[row + 1][idx + 1] + triangle[row][idx]
            dp[row][idx] = min(left, right)
    
    return dp[0][0]

if __name__ == '__main__':
    testCases = [
        [[2],[3,4],[6,5,7],[4,1,8,3]],  # 11
        [[-10]],                        # -10
    ]

    for i, triangle in enumerate(testCases):
        print(f'TestCase {i}: i/p: triangle = {triangle}; o/p: {minimumTotal(triangle)}')