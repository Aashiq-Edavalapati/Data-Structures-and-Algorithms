from .._01_Longest_Common_Subsequence._2_Top_Down import lcs

def lcps(s: str) -> int:
    return lcs(s, s[::-1])