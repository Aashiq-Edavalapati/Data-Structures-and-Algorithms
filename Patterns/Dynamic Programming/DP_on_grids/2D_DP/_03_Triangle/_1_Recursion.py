from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    rows = len(triangle)
    def helper(row, idx, pathSum):
        if row == rows - 1:
            return pathSum + triangle[row][idx]
        
        left = helper(row + 1, idx, pathSum + triangle[row][idx])
        right = helper(row + 1, idx + 1, pathSum + triangle[row][idx])

        return min(left, right)
    
    return helper(0, 0, 0)

if __name__ == '__main__':
    testCases = [
        [[2],[3,4],[6,5,7],[4,1,8,3]],  # 11
        [[-10]],                        # -10
    ]

    for i, triangle in enumerate(testCases):
        print(f'TestCase {i}: i/p: triangle = {triangle}; o/p: {minimumTotal(triangle)}')