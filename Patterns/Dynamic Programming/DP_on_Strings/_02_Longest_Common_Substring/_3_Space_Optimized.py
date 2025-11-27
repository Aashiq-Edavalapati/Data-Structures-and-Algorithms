def lcsubstr(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    prev = [0 for _ in range(n2 + 1)]
    maxCnt = 0
    for i in range(1, n1 + 1):
        curr = [0 for _ in range(n2 + 1)]
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                maxCnt = max(maxCnt, curr[j])
        prev = curr
    
    return maxCnt

if __name__ == '__main__':
    testCases = [
        ("abcjklp", "acjkp"),   # 3 (cjk)
        ("abcjelm", "adbcebcjek") # 4 (bcje)
    ]

    for i, testCase in enumerate(testCases):
        s1, s2 = testCase
        print(f"TestCase {i}: i/p: s1={s1}, s2={s2}; o/p: {lcsubstr(s1, s2)}")