# Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            elif len(stack)==0 or i != brackets[stack.pop()]:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    testCases = [
        "()", # true
        "()[]{}", # true
        "(]", # false
        "([])" # true
        "([)]", # false
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {sol.isValid(s)}")