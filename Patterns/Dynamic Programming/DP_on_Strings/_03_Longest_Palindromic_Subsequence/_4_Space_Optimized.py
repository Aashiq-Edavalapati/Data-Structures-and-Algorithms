from .._01_Longest_Common_Subsequence._4_Space_Optimized import lcs

def lcps(s: str) -> int:
    return lcs(s, s[::-1])