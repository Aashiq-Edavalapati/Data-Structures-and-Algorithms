# Link: https://leetcode.com/problems/fruit-into-baskets/

"""
    @question(LC 904):
        You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

        You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

            - You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
            
            - Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
            
            - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
        
        Given the integer array fruits, return the maximum number of fruits you can pick.

    -------------------------------------------------------------------
    -------------------------------------------------------------------

        Example 1:
            Input: fruits = [1,2,1]
            Output: 3
            Explanation: We can pick from all 3 trees.

        -------------------------------------------------------------------

        Example 2:
            Input: fruits = [0,1,2,2]
            Output: 3
            Explanation: We can pick from trees [1,2,2].
               If we had started at the first tree, we would only pick from trees [0,1].

        -------------------------------------------------------------------
        
        Example 3:
            Input: fruits = [1,2,3,2,2]
            Output: 4
            Explanation: We can pick from trees [2,3,2,2].
                If we had started at the first tree, we would only pick from trees [1,2].
        
    -------------------------------------------------------------------
    -------------------------------------------------------------------

        Constraints:
            1 <= fruits.length <= 105
            0 <= fruits[i] < fruits.length
"""
from typing import List

def totalFruit(fruits: List[int]) -> int:
    basket = {}
    l, r, maxFruits, currFruits =  0, 0, 0, 0
    n = len(fruits)
    while r < n:
        if fruits[r] in basket:
            basket[fruits[r]] += 1
            r += 1
            currFruits += 1
            maxFruits = max(maxFruits, currFruits)
        elif len(basket) < 2:
            basket[fruits[r]] = 1
            currFruits += 1
            r += 1
            maxFruits = max(maxFruits, currFruits)
        else:
            while True:
                basket[fruits[l]] -= 1
                currFruits -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                    l += 1
                    break
                l += 1
    
    return maxFruits

if __name__ == '__main__':
    testCases = [
        [1,2,1], # 3
        [0,1,2,2], # 3
        [1,2,3,2,2], # 4
    ]

    for i, fruits in enumerate(testCases):
        print(f"TestCase {i}:- i/p: fruits={fruits}; o/p: {totalFruit(fruits)}")