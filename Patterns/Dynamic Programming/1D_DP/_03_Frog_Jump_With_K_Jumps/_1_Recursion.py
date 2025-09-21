from typing import List

"""
    3 steps:
        1. Represent everything in terms of indices.
            0, 1, ...., n - 1 => Index of the array
        2. Do all possible stuffs acc. to the problem statement.
            Jump 1 step or Jump 2 steps or .... Jump k steps => f(n - 1) and f(n - 2) .... f(n - k)
        3. Min => Min(all stuffs)
            Min(f(n - 1), f(n - 2), ...., f(n - k))
"""

def minEnergy(ind: int, heights: List[int], k: int) -> int:
    if ind == 0: return 0

    minE = float('inf')
    for i in range(1, k + 1):
        if ind - i < 0: break
        minE = min(minE, minEnergy(ind - i, heights, k) + abs(heights[ind] - heights[ind - i]))

    return minE

if __name__ == '__main__':
    testCases = [
        ([10, 5, 20, 0, 15], 2),
        ([15, 4, 1, 14, 15], 3),
        ([15, 4, 1, 14, 15], 4)
    ]
    for i, inp in enumerate(testCases):
        heights, k = inp
        print(f'TestCase {i}: i/p: {heights} o/p: {minEnergy(len(heights) - 1, heights, k)}')