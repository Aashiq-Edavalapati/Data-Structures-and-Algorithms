# Link: https://leetcode.com/problems/longest-palindromic-subsequence/

from .._01_Longest_Common_Subsequence._1_Recursion import lcs

def lcps(s: str) -> int:
    return lcs(s, s[::-1])