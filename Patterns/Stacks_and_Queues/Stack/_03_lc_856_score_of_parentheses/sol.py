# Link: https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]

        for char in s:
            if char == '(':
                stk.append(0)
            else:
                curr = stk.pop()

                if curr == 0:
                    stk[-1] += 1
                else:
                    stk[-1] += curr * 2
        
        return stk[0]


if __name__ == '__main__':
    sol = Solution()

    testCases = [
        "()", # 1
        "(())", # 2
        "()()", # 2
        "((()))", # 4
        "((()))()(()())", # 9
        "(()(()))" # 6
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {sol.scoreOfParentheses(s)}")