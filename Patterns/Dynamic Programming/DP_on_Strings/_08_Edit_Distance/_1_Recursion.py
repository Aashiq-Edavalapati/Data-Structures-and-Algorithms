# Link: https://leetcode.com/problems/edit-distance/description/

"""
    @question:
        Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

        You have the following three operations permitted on a word:

        Insert a character
        Delete a character
        Replace a character
        
------------------------------------------------------------
        Example 1:
            Input: word1 = "horse", word2 = "ros"
            Output: 3
            Explanation: 
                horse -> rorse (replace 'h' with 'r')
                rorse -> rose (remove 'r')
                rose -> ros (remove 'e')
        ----------------------------------------------------
        Example 2:
            Input: word1 = "intention", word2 = "execution"
            Output: 5
            Explanation: 
                intention -> inention (remove 't')
                inention -> enention (replace 'i' with 'e')
                enention -> exention (replace 'n' with 'x')
                exention -> exection (replace 'n' with 'c')
                exection -> execution (insert 'u')
-------------------------------------------------------------------------------
        Constraints:
            0 <= word1.length, word2.length <= 500
            word1 and word2 consist of lowercase English letters.
"""

def editDistance(s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    def helper(i: int, j: int) -> int:
        # Base Cases
        if i < 0: # If i < 0 => 1st string finished, but still some chars might have been left out in the 2nd string =>            j + 1 insertions more
            return j + 1
        if j < 0: # If j < 0 => 2nd string finished, but still some chars are left out in the 1st string => i + 1               deletions
            return i + 1

        # If the curr chars match => No operation required => Move both i and j to next pos
        if s1[i] == s2[j]:
            return helper(i - 1, j - 1)
        
        # Choice 1: Insertion => Insert s2[j] after s1[i], then s1[i + 1] and s2[j] match now => Char match case for `i + 1` and `j` => f((i + 1) - 1, j - 1)
        insert = 1 + helper(i, j - 1)
        # Choice 2: Deletion => Delete s1[i] => s2[j] is yet to be matched => Move only i to next pos
        delete = 1 + helper(i - 1, j) 
        # Choice 3: Replace => Replace s1[i] with s2[j] => Match case for `i` and `j` => f(i - 1, j - 1)
        replace = 1 + helper(i - 1, j - 1)

        # Return min(all possible paths)
        return min(insert, delete, replace)
    
    return helper(n1 - 1, n2 - 1)

if __name__ == '__main__':
    testCases = [
        ("horse", "ros"),   # 3
        ("intention", "execution"), # 5
    ]

    for i, testCase in enumerate(testCases):
        s1, s2 = testCase
        print(f"TestCase {i}: i/p: s1={s1}, s2={s2}; o/p: {editDistance(s1, s2)}")