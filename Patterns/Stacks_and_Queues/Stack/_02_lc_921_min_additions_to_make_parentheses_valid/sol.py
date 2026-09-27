# Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        mismatch = 0
        for char in s:
            if char == '(':
                stack.append(char)
            elif len(stack) > 0:
                stack.pop()
            else:
                mismatch += 1
        
        return len(stack) + mismatch

if __name__ == '__main__':
    sol = Solution()

    testCases = [
        "())", # 1
        "(((", # 3
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {sol.minAddToMakeValid(s)}")