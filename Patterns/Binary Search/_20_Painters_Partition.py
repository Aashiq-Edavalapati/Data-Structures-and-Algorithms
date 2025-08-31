# -----------------------------------------------------------------------------
# Problem: Painter's Partition   ||   Split Array - Largest Sum
# -----------------------------------------------------------------------------
#
# @question:
#   You are given an array `arr` of non-negative integers and an integer `k`.
#   You need to divide the array into `k` or fewer continuous subarrays.
#   The goal is to minimize the largest sum among these subarrays.
#
#   Return this minimum largest sum.
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Answer
#   - We are not looking for an element inside the array.
#   - We are searching for the minimum possible "largest subarray sum".
#   - Monotonic property:
#       If we can split the array into ≤ k partitions with sum ≤ X,
#       then any larger X also works.
#       If we cannot do it with X, then any smaller X also fails.
#   - This monotonicity → perfect for binary search.
#
# -----------------------------------------------------------------------------
# @method (easy steps):
#   1. The minimum possible max sum is max(arr) 
#        (because one partition must at least hold the largest element).
#   2. The maximum possible max sum is sum(arr) 
#        (if we put all elements into one partition).
#   3. Binary search between [max(arr), sum(arr)]:
#        - For mid = candidate max sum, check how many partitions are needed
#          (each partition ≤ mid).
#        - If partitions needed ≤ k → try smaller max sum (move right).
#        - Else → need larger max sum (move left).
#   4. At the end, `left` will hold the minimum largest sum possible.
#
# Time Complexity: O(N log(sum(arr) - max(arr)))
# Space Complexity: O(1)
# ==============================================================================

def numPartitions(arr, maxSum):
    """
    Given a max allowed sum (maxSum), return the number of partitions needed
    so that no partition exceeds maxSum.
    """
    currSum = arr[0]
    i = 1
    partitions = 1  # start with the first partition

    while i < len(arr):
        currSum += arr[i]
        # If adding this element exceeds maxSum, start a new partition
        if currSum > maxSum:
            currSum = arr[i]
            partitions += 1
        i += 1

    return partitions

def minMaxSum(arr, k):
    """
    Find the minimum possible largest sum when splitting array into ≤ k partitions.
    """
    left, right = max(arr), sum(arr)

    while left <= right:
        mid = left + (right - left) // 2

        if numPartitions(arr, mid) <= k:
            # If we can split within k partitions, try smaller max sum
            right = mid - 1
        else:
            # Otherwise, need to allow larger max sum
            left = mid + 1
    
    # The minimum largest sum is stored in `left`
    return left

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    testCases = [
        ([10, 20, 30, 40], 2)
    ]

    i = 0
    for arr, k in testCases:
        print(f'TestCase {i}: {minMaxSum(arr, k)}')
        i += 1
