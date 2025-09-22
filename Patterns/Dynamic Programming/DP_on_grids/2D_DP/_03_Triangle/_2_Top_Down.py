from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    rows = len(triangle)
    dp = [[-1 for _ in range(rows)] for _ in range(rows)]
    def helper(row, idx, pathSum):
        if row == rows - 1:
            return pathSum + triangle[row][idx]
        if dp[row][idx] != -1: return dp[row][idx]
        
        left = helper(row + 1, idx, pathSum + triangle[row][idx])
        right = helper(row + 1, idx + 1, pathSum + triangle[row][idx])

        dp[row][idx] = min(left, right)
        return dp[row][idx]
    
    return helper(0, 0, 0)

if __name__ == '__main__':
    testCases = [
        [[2],[3,4],[6,5,7],[4,1,8,3]],  # 11
        [[-10]],                        # -10
    ]

    for i, triangle in enumerate(testCases):
        print(f'TestCase {i}: i/p: triangle = {triangle}; o/p: {minimumTotal(triangle)}')