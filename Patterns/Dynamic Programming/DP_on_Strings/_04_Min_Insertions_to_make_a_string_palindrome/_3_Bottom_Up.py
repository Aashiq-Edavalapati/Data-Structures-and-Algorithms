from .._03_Longest_Common_Palindromic_Subsequence._3_Bottom_Up import lcps

def minInsertions(s: str) -> int:
    n = len(s)
    return n - lcps(s)