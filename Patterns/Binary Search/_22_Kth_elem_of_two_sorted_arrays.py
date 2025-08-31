# -----------------------------------------------------------------------------
# Problem: K-th Element of Two Sorted Arrays
# -----------------------------------------------------------------------------
#
# @question:
#   You are given two sorted arrays `arr1` and `arr2`, and an integer `k`.
#   Find the k-th smallest element in the combined sorted array (without merging).
#
# -----------------------------------------------------------------------------
# @pattern: Binary Search on Answer
#   - Instead of merging arrays (O(n1+n2)), we use binary search.
#   - Idea: Partition both arrays so that the left half contains exactly k elements.
#   - Then the k-th element will be the maximum of the left partition.
#
# -----------------------------------------------------------------------------
# @method (step-by-step):
#   1. Always binary search on the smaller array.
#   2. Search space for arr1’s contribution = [max(0, k-n2), min(n1, k)].
#        - Because arr1 can give at most k elements, and at least k-n2 elements.
#   3. For mid1 in arr1, let mid2 = k - mid1.
#   4. Define:
#        l1 = arr1[mid1-1] if mid1 > 0 else -∞
#        r1 = arr1[mid1] if mid1 < n1 else +∞
#        l2 = arr2[mid2-1] if mid2 > 0 else -∞
#        r2 = arr2[mid2] if mid2 < n2 else +∞
#   5. Partition check:
#        - If l1 > r2 → move search left.
#        - If l2 > r1 → move search right.
#        - Else → valid partition found, answer = max(l1, l2).
#
# Time Complexity: O(log(min(n1, n2)))
# Space Complexity: O(1)
# ==============================================================================

def kthElement(arr1, arr2, k):
    n1 = len(arr1)
    n2 = len(arr2)
    # Always search in smaller array
    if n1 > n2: 
        return kthElement(arr2, arr1, k)

    left, right = max(0, k - n2), min(n1, k)

    while left <= right:
        mid1 = left + (right - left) // 2
        mid2 = k - mid1  # remaining elements come from arr2

        # Set boundaries
        l1, l2 = float('-inf'), float('-inf')
        r1, r2 = float('inf'), float('inf')

        if mid1 < n1: 
            r1 = arr1[mid1]
        if mid2 < n2: 
            r2 = arr2[mid2]
        if mid1 > 0: 
            l1 = arr1[mid1 - 1]
        if mid2 > 0: 
            l2 = arr2[mid2 - 1]

        # Adjust search
        if l1 > r2:
            right = mid1 - 1  # move left
        elif l2 > r1:
            left = mid1 + 1   # move right
        else:
            # Correct partition → kth element
            return max(l1, l2)

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    testCases = [
        ([2, 3, 6, 7, 9], [1, 4, 8, 10], 4),   # 4th element in merged array
    ]

    i = 0
    for arr1, arr2, k in testCases:
        print(f'TestCase {i}: {kthElement(arr1, arr2, k)}')
        i += 1
