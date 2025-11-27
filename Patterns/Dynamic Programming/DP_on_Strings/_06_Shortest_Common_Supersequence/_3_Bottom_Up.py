# Link: https://leetcode.com/problems/shortest-common-supersequence/

def scsq(str1: str, str2: str):
    n1, n2 = len(str1), len(str2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    i, j = n1, n2
    res = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            res.append(str1[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                res.append(str2[j - 1])
                j -= 1
            elif dp[i][j - 1] < dp[i - 1][j]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str1[i - 1])
                i -= 1
    if i == 0 and j > 0:
        while j > 0:
            res.append(str2[j - 1])
            j -= 1
    elif j == 0 and i > 0:
        while i > 0:
            res.append(str1[i - 1])
            i -= 1

    return ''.join(res[::-1])

if __name__ == '__main__':
    testCases = [
        ("brute", "groot"), # len 8
        ("abac", "cab"),    # len 5
        ("aaaaaaaa", "aaaaaaaa"),   # len 8
        ("bbbaaaba", "bbababbb"),   # len 11
    ]

    for i, testCase in enumerate(testCases):
        str1, str2 = testCase
        print(f"TestCase {i}: i/p: str1={str1}, str2={str2}; o/p: {scsq(str1, str2)}")