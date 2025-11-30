# Link: https://leetcode.com/problems/palindrome-partitioning-ii/

"""
    @question:
        Given a string s, partition s such that every substring of the partition is a palindrome.

        Return the minimum cuts needed for a palindrome partitioning of s.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Example 1:
            Input: s = "aab"
            Output: 1
            Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
    
        -------------------------------------------------------------------------------

        Example 2:
            Input: s = "a"
            Output: 0
        
        -------------------------------------------------------------------------------

        Example 3:
            Input: s = "ab"
            Output: 1
        
    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Constraints:
            1 <= s.length <= 2000
            s consists of lowercase English letters only.
"""

"""
    @intuition:
        - We are trying to partition the string into substrings where each substring is a palindrome.
          i.e., we can make a partition at an index only if the substring till that is a palindrome.
          So, we can start from the start and then from that we see all possible partitions starting from that index.

        - After doing each partition we increase the partition count by 1 and do a recursive call for finding min no. of partitions for the remaining substring(subproblem).

        - i.e., the reccurence would be like:
            f(i) {
                if (i == n) return 0;

                minCuts = INF
                for (j = i -> n) {
                    if (isPalindrome(i, j, s)) {
                        cuts = 1 + f(j + 1)
                        minCuts = min(minCuts, cuts)
                    }
                }

                return minCuts
            }
"""
def minCuts(s: str) -> int:
    n = len(s)
    def helper(i: int) -> int:
        # Base Case: i = n => Exhausted full string
        if i == n: return 0

        minCut = float('inf')
        for j in range(i, n):
            if isPalindrome(i, j, s):
                cuts = 1 + helper(j + 1)
                minCut = min(minCut, cuts)
        
        return minCut

    return helper(0) - 1

def isPalindrome(i: int, j: int, s: str) -> bool:
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    
    return True

if __name__ == '__main__':
    testCases = [
        "aab", # 1
        "a", # 0
        "ab", # 1
        "abaaba", # 0
    ]

    for i, s in enumerate(testCases):
        print(f"TestCase {i}:- i/p: s={s}; o/p: {minCuts(s)}")