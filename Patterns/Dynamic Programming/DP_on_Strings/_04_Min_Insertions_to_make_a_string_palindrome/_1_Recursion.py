# Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

from .._03_Longest_Common_Palindromic_Subsequence._1_Recursion import lcps

def minInsertions(s: str) -> int:
    n = len(s)
    return n - lcps(s)