# Link: https://leetcode.com/problems/longest-string-chain/

"""
    @question:
        You are given an array of words where each word consists of lowercase English letters.

        wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

        For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
        A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

        Return the length of the longest possible word chain with words chosen from the given list of words.

        Example 1:
            Input: words = ["a","b","ba","bca","bda","bdca"]
            Output: 4
            Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

        ----------------------------------------------------------------------------
            
        Example 2:
            Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
            Output: 5
            Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

        ----------------------------------------------------------------------------

        Example 3:
            Input: words = ["abcd","dbqca"]
            Output: 1
            Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
            ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
        
    -------------------------------------------------------------------------------------------------------

        Constraints:
            1 <= words.length <= 1000
            1 <= words[i].length <= 16
            words[i] only consists of lowercase English letters.
"""
from typing import List

def longestStrChain(words: List[str]) -> int:
    words.sort(key=lambda word : len(word))
    n = len(words)
    dp = [1] * n
    for i in range(1, n):
        for prev in range(i):
            if _isPredecessor(words[prev], words[i]):
                dp[i] = max(dp[i], 1 + dp[prev])
    
    return dp[-1]

def _isPredecessor(a: str, b: str) -> bool:
    n, m = len(a), len(b)
    if n != m - 1: return False
    i, j = 0, 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            j += 1
        elif j - i > 1: return False
        else:
            j += 1

    return i == n

if __name__ == '__main__':
    testCases = [
        ["a","b","ba","bca","bda","bdca"], # 4
        ["xbc","pcxbcf","xb","cxbc","pcxbc"], # 5
        ["abcd","dbqca"], # 1
    ]

    for i, words in enumerate(testCases):
        print(f"TestCase {i}: i/p: words={words}; o/p: {longestStrChain(words)}")