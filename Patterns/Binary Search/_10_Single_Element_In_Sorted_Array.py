from typing import List

# -----------------------------------------------------------------------------
# Problem: Single Element in a Sorted Array
# -----------------------------------------------------------------------------
#
# @question:
#   You are given a sorted array where every element appears exactly twice,
#   except for one element which appears exactly once.
#   Find and return that single element.
#
# -----------------------------------------------------------------------------
# @pattern:
#   The array is sorted with a strict pairing pattern (every element appears twice, except one). 
#   This creates a monotonic property in index parity: before the single element, pairs start at even indices; 
#   after it, pairs start at odd indices. 
#   Detecting where this pattern breaks lets you discard half of the array each step → Binary Search applies.
# -----------------------------------------------------------------------------
#
# @method:
#   1. If the single element is at the edges, handle it as a special case.
#   2. For elements in the middle, use binary search and rely on index parity:
#      - In a perfectly paired array, the first element of each pair is at
#        an even index, and the second at an odd index.
#      - If pairing breaks at some point, the single element lies before it.
#   3. Adjust search boundaries accordingly.
#
# -----------------------------------------------------------------------------
# Intuition:
#   By exploiting the sorted nature and the pairing pattern, we can ignore half
#   of the array in each step, achieving O(log n) performance.
# -----------------------------------------------------------------------------

def bruteForceSingleElement(arr: List[int]) -> int:
    """
    Brute force approach to find the single element.

    Parameters:
        arr (List[int]): Sorted list where every element appears twice except one.

    Returns:
        int: The single element.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for num in arr:
        if arr.count(num) == 1:
            return num
    return -1


def findSingleElement(arr: List[int]) -> int:
    """
    Finds the single element in a sorted array where every other element appears twice.

    Parameters:
        arr (List[int]): Sorted list where every element appears twice except one.

    Returns:
        int: The single element.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    n = len(arr)

    # Edge cases: single element or single at array ends
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    
    left, right = 1, n - 2
    while left <= right:
        mid = left + (right - left) // 2

        # Found the single element
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        
        # Check pairing pattern based on mid index parity
        if mid % 2 == 0:
            if arr[mid] == arr[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] == arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


# -----------------------------------------------------------------------------
# Driver Code with Test Cases
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("--- Testing Single Element in Sorted Array ---")
    test_cases = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1], 1),                           # Single element only
        ([0, 0, 1], 1),                     # Single at end
        ([1, 2, 2], 1)                      # Single at start
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Array: {arr}")

        brute_result = bruteForceSingleElement(arr)
        binary_result = findSingleElement(arr)

        print(f"Brute Force Result: {brute_result}")
        print(f"Binary Search Result: {binary_result}")
        print(f"Expected: {expected}")

        if brute_result == binary_result == expected:
            print("✅ Results match expected output!")
        else:
            print("❌ Mismatch detected!")
