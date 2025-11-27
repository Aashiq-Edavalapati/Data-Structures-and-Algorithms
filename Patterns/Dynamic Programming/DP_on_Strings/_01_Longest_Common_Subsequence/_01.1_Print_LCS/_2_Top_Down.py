from typing import List

def printLCS(str1: str, str2: str) -> str:
    paths = []
    currMax = [0]
    dp = [[-1 for _ in range(len(str2))] for _ in range(len(str1))]
    def helper(i: int, j: int, path: List[str]) -> int:
        if i < 0 or j < 0:
            if len(path) > currMax[0]:
                currMax[0] = len(path)
                paths.append("".join(path[::-1]))
            return 0
        
        if str1[i] == str2[j]:
            path.append(str1[i])
            size = 1 + helper(i - 1, j - 1, path)
            path.pop()
            return size
        if dp[i][j] != -1: return dp[i][j]

        left = helper(i - 1, j, path[:])
        right = helper(i, j - 1, path[:])

        return max(left, right)

    path = []
    size = helper(len(str1) - 1, len(str2) - 1, path)
    print(size)
    return list(set(["".join(seq) for seq in paths if len(seq) == size]))

if __name__ == '__main__':
    testCases = [
        ("bdefg", "bfg"),   # bfg
        ("mnop", "mnq"),    # mn
    ]

    for i, testCase in enumerate(testCases):
        str1, str2 = testCase
        print(f'TestCase{i}: i/p: str1={str1}, str2={str2}; o/p: {printLCS(str1, str2)}')