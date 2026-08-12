# Link: https://leetcode.com/problems/longest-common-prefix/

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    first, last = strs[0], strs[-1]
    i = 0

    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return strs[0][:i]

if __name__ == '__main__':
    testCases = [
        ["flower","flow","flight"], # "fl"
        ["dog","racecar","car"], # ""
        ["ab", "a"], # "a"
    ]

    for i, strs in enumerate(testCases):
        print(f"Testcase {i}:- i/p: strs={strs}; o/p: {longestCommonPrefix(strs)}")