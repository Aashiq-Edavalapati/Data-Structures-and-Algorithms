from typing import List

def lcstr(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)

    def helper(i: int, j: int, cnt: int) -> int:
        # Base case: Ran out of string. The max length found on this path is the count we ended with.
        if i < 0 or j < 0:
            return cnt

        # 1. We must always consider starting fresh from new positions, as the longest string might be somewhere else.
        res_new_path_1 = helper(i - 1, j, 0)
        res_new_path_2 = helper(i, j - 1, 0)

        # 2. We also consider the *current* path
        current_path_res = cnt # Start with the length we have so far
        if s1[i] == s2[j]:
            # If we match, the result of this path is whatever we find by continuing it.
            current_path_res = helper(i - 1, j - 1, cnt + 1)
        
        # The final result is the maximum of all possibilities:
            # - The max from starting fresh at (i-1, j)
            # - The max from starting fresh at (i, j-1)
            # - The max from continuing (or ending) the current path
        return max(current_path_res, res_new_path_1, res_new_path_2)

    return helper(n1 - 1, n2 - 1, 0)

"""
    Otherwise, the most obvious approach would be to keep an additional non local variable to keep track of the max length till now!
"""

if __name__ == '__main__':
    testCases = [
        ("abcjklp", "acjkp"),   # 2 (jk)
        ("abcjelm", "adbcebcjek") # 4 (bcje)

    ]

    for i, testCase in enumerate(testCases):
        s1, s2 = testCase
        print(f"TestCase {i}: i/p: s1={s1}, s2={s2}; o/p: {lcstr(s1, s2)}")