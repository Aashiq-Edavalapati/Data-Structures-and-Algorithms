# Link: https://leetcode.com/problems/sum-of-subarray-minimums/

"""
    @question:
        Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
 
    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Example 1:
            Input: arr = [3,1,2,4]
            Output: 17
            Explanation: 
                Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
                Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
                Sum is 17.

        -------------------------------------------------------------------------------
                
        Example 2:
            Input: arr = [11,81,94,43,3]
            Output: 444
        
    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------
            
        Constraints:
            1 <= arr.length <= 3 * 104
            1 <= arr[i] <= 3 * 104
"""
from typing import List

"""
    @intuition:
        For each index, we try to check how far we can extend the subarray for the curr element to be min in that subarray.
        Once we find that we can say that all the possible subarrays in that subarray will have curr element as min value
"""
def sumSubarrayMins1(arr: List[int]) -> int:
    MOD = 10 ** 9 + 7
    n = len(arr)
    nse = findNSE(arr)
    psee = findPSEE(arr)
    ans = 0
    for i in range(n):
        left = i - psee[i]
        right = nse[i] - i
        ans = (ans + (left * right * arr[i]) % MOD) % MOD
    
    return ans


def findNSE(arr):
    n = len(arr)
    nse = [n] * n
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] >= arr[i]:
            stk.pop()
        if stk:
            nse[i] = stk[-1]
        stk.append(i)
    
    return nse

def findPSEE(arr):
    n = len(arr)
    psee = [-1] * n
    stk = []
    for i in range(n):
        while stk and arr[stk[-1]] > arr[i]:
            stk.pop()
        if stk:
            psee[i] = stk[-1]
        stk.append(i)
    
    return psee

def sumSubarrayMins(arr: List[int]) -> int:
    MOD = 10 ** 9 + 7
    n = len(arr)
    stk = []
    ans = 0
    arr.append(0) # Add 0 at the end to flush the stack instead of extra loop at the end
    for i in range(n + 1):
        while stk and arr[stk[-1]] >= arr[i]:
            idx = stk.pop()
            left = idx - (stk[-1] if stk else -1)
            right = i - idx

            ans = (ans + (arr[idx] * left * right) % MOD) % MOD
        stk.append(i)
    
    # while stk:
    #     idx = stk.pop()
    #     left = idx - (stk[-1] if stk else -1)
    #     right = n - idx

    #     ans = (ans + (arr[idx] * left * right) % MOD) % MOD

    return ans

if __name__ == '__main__':
    testCases = [
        [3,1,2,4], # 17
        [11,81,94,43,3], # 444
        [1,4,6,7,3,7,8,1], # 104
    ]

    for i, arr in enumerate(testCases):
        print(f"TestCase {i}:- i/p: arr={arr}; o/p: {sumSubarrayMins(arr)}")