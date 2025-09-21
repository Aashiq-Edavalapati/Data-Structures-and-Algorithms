from typing import List

def maxNonAdjSum(arr: List[int]) -> int:
    n = len(arr) 
    prev, prev2 = arr[0], 0
    for i in range(1, n):
        curr = max(arr[i] + prev2, prev)
        prev2 = prev
        prev = curr

    return prev

def houseRobber2(arr: List[int]) -> int:
    arr1 = arr[1:]
    arr2 = arr[:-1]
    return max(maxNonAdjSum(arr1), maxNonAdjSum(arr2))


if __name__ == '__main__':
    testCases = [
        [2,3,2], # 3
        [1, 2, 3], # 3
        [1,2,3,1], # 4
        [2,7,9,3,1] # 11
    ]
    for i, arr in enumerate(testCases):
        print(f'TestCase {i}: i/p: {arr} o/p: {houseRobber2(arr)}')