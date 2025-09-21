from typing import List

"""
    3 steps:
        1. Represent everything in terms of indices.
            0, 1, ...., n - 1 => Index of the array
        2. Do all possible stuffs acc. to the problem statement.
            Pick or Not Pick: (f(i - 2) + arr[i]) or (f(i - 1))
        3. Max => Max(all stuffs)
            Max((f(i - 2) + arr[i]), (f(i - 1)))
"""

def houseRobber2(arr: List[int]) -> int:
    def helper(ind: int, arr: List[int]):
        if ind == 0: return arr[0] # Base Case
        if ind < 0: return 0 # Base Case

        pick = arr[ind] + helper(ind - 2, arr)
        notPick = helper(ind - 1, arr)

        return max(pick, notPick)

    return max(helper(len(arr) - 2, arr[:-1]), helper(len(arr) - 2, arr[1:]))

# Alternative solution
def maxNonAdjSum2(ind: int, arr: List[int], robbedLast: bool) -> int:
    if ind == 0:
        # Base Case
        if robbedLast:
            return 0
        return arr[0]
    if ind < 0: return 0

    # Pick the current element => Skip the next element
    pick = maxNonAdjSum2(ind - 2, arr, robbedLast) + arr[ind]
    if ind == len(arr) - 1: pick = arr[ind] + maxNonAdjSum2(ind - 2, arr, True)

    # Not picking the current element => Try the next element
    notPick = maxNonAdjSum2(ind - 1, arr, robbedLast)
    
    # Return the maximum of both
    return max(pick, notPick)

if __name__ == '__main__':
    testCases = [
        [2,3,2], # 3
        [1, 2, 3], # 3
        [1,2,3,1], # 4
        [2,7,9,3,1] # 11
    ]
    for i, arr in enumerate(testCases):
        # print(f'TestCase {i}: i/p: {arr} o/p: {maxNonAdjSum(len(arr) - 1, arr, False)}')
        print(f'TestCase {i}: i/p: {arr} o/p: {houseRobber2(arr)}')