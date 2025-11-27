from .._03_Longest_Common_Palindromic_Subsequence._4_Space_Optimized import lcps

def minInsertions(s: str) -> int:
    n = len(s)
    return n - lcps(s)