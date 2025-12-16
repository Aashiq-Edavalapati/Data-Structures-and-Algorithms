# Link: https://leetcode.com/problems/remove-k-digits/

"""
    @question(LC 402):
        Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

    =========================================================================
    =========================================================================
    
        Example 1:
            Input: num = "1432219", k = 3
            Output: "1219"
            Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

        =========================================================================

        Example 2:
            Input: num = "10200", k = 1
            Output: "200"
            Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

        =========================================================================

        Example 3:
            Input: num = "10", k = 2
            Output: "0"
            Explanation: Remove all the digits from the number and it is left with nothing which is 0.
        
        =========================================================================
        =========================================================================

        Constraints:
            1 <= k <= num.length <= 105
            num consists of only digits.
            num does not have any leading zeros except for the zero itself.
"""
from typing import List

def removeKDigits(num: str, k: int) -> str:
    n = len(num)
    stk = []
    i = 0
    while i < n and k > 0:
        while stk and stk[-1] > num[i]:
            if k < 1: break
            stk.pop()
            k -= 1
        stk.append(num[i])
        i += 1
    stk = stk[:-k] if k > 0 else stk
    while stk and stk[0] == '0':
        stk.pop(0)
    res = ''.join(stk) + (num[i:] if i < n else "")

    return res if res else "0"

if __name__ == '__main__':
    testCases = [
        ("1432219", 3), # "1219"
        ("10200", 1), # "200"
        ("10", 2), # "0"
    ]

    for i, testCase in enumerate(testCases):
        num, k = testCase
        print(f"TestCase {i}:- i/p: num={num}, k={k}; o/p: {removeKDigits(num, k)}")