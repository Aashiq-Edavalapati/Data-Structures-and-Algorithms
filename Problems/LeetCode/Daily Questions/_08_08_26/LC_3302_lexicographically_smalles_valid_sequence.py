# Link: https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

from typing import List

def validSequence(word1: str, word2: str) -> List[int]:
    m, n = len(word1), len(word2)
    suffixMatch = [0] * (m + 1)
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        suffixMatch[i] = suffixMatch[i + 1]
        if word1[i] == word2[j]:
            suffixMatch[i] += 1
            i -= 1
            j -= 1
        else:
            i -= 1

    while i >= 0:
        suffixMatch[i] = suffixMatch[i + 1]
        i -= 1

    i, j = 0, 0
    seq = []
    edited = False
    while i < m and j < n:
        if word1[i] == word2[j]:
            seq.append(i)
            j += 1
        elif not edited and suffixMatch[i + 1] >= n - j - 1:
            seq.append(i)
            edited = True
            j += 1
        if len(seq) == n: return seq
        i += 1
    
    return []

if __name__ == "__main__":
    testCases = [
        ["vbcca", "abc"], # [0, 1, 2]
        ["bacdc", "abc"], # [1, 2, 4]
        ["aaaaaa", "aaabc"], # []
        ["abc", "ab"], # [0, 1]
        ["ccbccccbcc", "b"], # [0]
    ]

    for i, (word1, word2) in enumerate(testCases):
        print(f"Test Case {i + 1}: Input: word1 = {word1}, word2 = {word2} => Output: {validSequence(word1, word2)}")