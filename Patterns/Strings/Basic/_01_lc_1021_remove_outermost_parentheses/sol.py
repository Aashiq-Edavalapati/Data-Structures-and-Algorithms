# Link: https://leetcode.com/problems/remove-outermost-parentheses/

def removeOuterParentheses(s: str) -> str:
    openCnt = 0
    stk = []

    for par in s:
        if par == '(' and openCnt > 0:
            stk.append('(')
        elif par == ')' and openCnt > 1:
            stk.append(')')

        if par == '(':
            openCnt += 1
        else:
            openCnt -= 1

    return ''.join(stk)


if __name__ == '__main__':
    testCases = [
        "(()())(())", # "()()()"
        "(()())(())(()(()))", # "()()()()(())"
        "()()", # ""
    ]

    for i, s in enumerate(testCases):
        print(f"Testcase {i}:- i/p: s={s}; o/p: {removeOuterParentheses(s)}")