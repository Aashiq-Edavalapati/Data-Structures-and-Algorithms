from typing import List

"""
    3 steps:
        1. Represent everything in terms of indices.
            0, 1, ...., n - 1 => Index of the array
        2. Do all possible stuffs acc. to the problem statement.
            Pick or Not Pick: (f(i + 2) + arr[i]) or (f(i + 1))
        3. Max => Max(all stuffs)
            Max((f(i + 2) + arr[i]), (f(i + 1)))
"""

def maxNonAdjSum(ind: int, arr: List[int], n: int) -> int:
    if ind >= n:    # Base Case
        return 0

    # Pick the current element => Skip the next element
    pick = maxNonAdjSum(ind + 2, arr, n) + arr[ind]

    # Not picking the current element => Try the next element
    notPick = maxNonAdjSum(ind + 1, arr, n)
    
    # Return the maximum of both
    return max(pick, notPick)

if __name__ == '__main__':
    testCases = [
        [1,2,3,1],
        [2,7,9,3,1]
    ]
    for i, arr in enumerate(testCases):
        print(f'TestCase {i}: i/p: {arr} o/p: {maxNonAdjSum(0, arr, len(arr))}')