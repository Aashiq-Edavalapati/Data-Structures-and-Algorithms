from .._03_Longest_Common_Palindromic_Subsequence._2_Top_Down import lcps

def minInsertions(s: str) -> int:
    n = len(s)
    return n - lcps(s)