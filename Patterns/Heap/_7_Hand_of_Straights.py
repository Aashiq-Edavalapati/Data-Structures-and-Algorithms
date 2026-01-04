# Link: https://leetcode.com/problems/hand-of-straights/

"""
    @question(LC 846):
        Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

        Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

    =========================================================================
    =========================================================================

        Example 1:
            Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
            Output: true
            Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

        =========================================================================

        Example 2:
            Input: hand = [1,2,3,4,5], groupSize = 4
            Output: false
            Explanation: Alice's hand can not be rearranged into groups of 4.

    =========================================================================
    =========================================================================

        Constraints:
            1 <= hand.length <= 104
            0 <= hand[i] <= 109
            1 <= groupSize <= hand.length
"""
from typing import List
from collections import defaultdict
import heapq

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0: return False

    freq = defaultdict(int)
    for card in hand:
        freq[card] += 1
    
    pq = []
    for card, f in freq.items():
        heapq.heappush(pq, (card, f))
    
    while pq:
        cnt = groupSize
        temp = []
        prev = pq[0][0] - 1
        while pq and cnt > 0:
            card, f = heapq.heappop(pq)
            if card - prev != 1: return False
            prev = card
            f -= 1
            if f != 0: temp.append((card, f))
            cnt -= 1
        if cnt > 0: return False
        for e in temp:
            heapq.heappush(pq, e)

    return True

if __name__ == '__main__':
    testCases = [
        ([1,2,3,6,2,3,4,7,8], 3), # True
        ([1,2,3,4,5], 4), # False
    ]

    for i, testCase in enumerate(testCases):
        hand, groupSize = testCase
        print(f"TestCase {i}:- i/p: hand={hand}, groupSize={groupSize}; o/p: {isNStraightHand(hand, groupSize)}")