from .._01_Longest_Common_Subsequence._3_Bottom_Up import lcs

def lcps(s: str) -> int:
    return lcs(s, s[::-1])