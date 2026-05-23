# Link: https://www.geeksforgeeks.org/problems/alien-dictionary/1

"""
    @question:
        A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.

        Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.

        However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").

            A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

        Note: Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false.

    -----------------------------------------------------------------------------
    -----------------------------------------------------------------------------
        
        Examples:
            Input: words[] = ["baa", "abcd", "abca", "cab", "cad"]
            Output: true
            Explanation: 
                A possible correct order of letters in the alien dictionary is "bdac".
                The pair "baa" and "abcd" suggests 'b' appears before 'a' in the alien dictionary.
                The pair "abcd" and "abca" suggests 'd' appears before 'a' in the alien dictionary.
                The pair "abca" and "cab" suggests 'a' appears before 'c' in the alien dictionary.
                The pair "cab" and "cad" suggests 'b' appears before 'd' in the alien dictionary.
                So, 'b' → 'd' → 'a' → 'c' is a valid ordering.

            -----------------------------------------------------------------------------
                
            Input: words[] = ["caa", "aaa", "aab"]
            Output: true
            Explanation:
                A possible correct order of letters in the alien dictionary is "cab".
                The pair "caa" and "aaa" suggests 'c' appears before 'a'.
                The pair "aaa" and "aab" suggests 'a' appear before 'b' in the alien dictionary. 
                So, 'c' → 'a' → 'b' is a valid ordering.

            -----------------------------------------------------------------------------
                
            Input: words[] = ["ab", "cd", "ef", "ad"]
            Output: ""
            Explanation: 
                No valid ordering of letters is possible.
                The pair "ab" and "ef" suggests "a" appears before "e".
                The pair "ef" and "ad" suggests "e" appears before "a", which contradicts the ordering rules.

    -----------------------------------------------------------------------------
    -----------------------------------------------------------------------------
                
        Constraints:
            1 ≤ words.length ≤ 500
            1 ≤ words[i].length ≤ 100
            words[i] consists only of lowercase English letters.
"""
from typing import List
from collections import deque

def findOrder(words: List[str]) -> str:
    """
        @intuition:
            - Since this question includes ordering of things => Topological sorting
    """
    n = len(words)
    adj_list = [[] for _ in range(26)]
    indegree = [0] * 26
    letters = set()
    for word in words:
        for char in word:
            letters.add(ord(char) - ord('a'))
    
    for i in range(n - 1):
        s1, s2 = words[i], words[i + 1]
        j = min(len(s1), len(s2))
        
        idx = 0
        while idx < j:
            if s1[idx] != s2[idx]:
                adj_list[ord(s1[idx]) - ord('a')].append(ord(s2[idx]) - ord('a'))
                indegree[ord(s2[idx]) - ord('a')] += 1
                break
            idx += 1
        
        if idx == j and len(s1) > len(s2): return ""
    
    q = deque()
    for letter in letters:
        if indegree[letter] == 0: q.append(letter)
        
    seq = []
    while q:
        letter = q.popleft()
        seq.append(chr(ord('a') + letter))
        for neighbor in adj_list[letter]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0: q.append(neighbor)
    
    return ''.join(seq) if len(seq) == len(letters) else ""


if __name__ == '__main__':
    testCases = [
        ["baa", "abcd", "abca", "cab", "cad"],
        ["caa", "aaa", "aab"],
        ["ab", "cd", "ef", "ad"]
    ]

    for i, words in enumerate(testCases):
        print(f"TestCase {i}: i/p: words={words}; o/p: {findOrder(words)}")