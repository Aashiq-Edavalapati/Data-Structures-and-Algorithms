import math
from typing import List

# -----------------------------------------------------------------------------
# Problem: Smallest Divisor Given a Threshold
# -----------------------------------------------------------------------------
#
# @question:
#   Given an array of integers `nums` and an integer `threshold`, we will
#   choose a positive integer `divisor`, divide all the array elements by
#   it, and sum the ceiling of the division results. Find the smallest
#   `divisor` such that the result of the sum is less than or equal to
#   `threshold`.
#
# ------------------------------------------------------------------------------
#
# @pattern: Min. Value that satisfies a given condition
#
# ------------------------------------------------------------------------------
#
# @method: Binary Search on Answer
#
# ===============================================================================

def bruteForce(nums: List[int], threshold: int) -> int:
    """
        Finds the smallest divisor using a brute-force linear search.

        This function iterates through all possible divisors starting from 1 up to
        the largest number in the array. For each divisor, it calculates the sum
        of the ceilings and returns the first divisor that meets the threshold
        condition.

        Time Complexity: O(N * M), where N is the maximum value in the array and M
                        is the number of elements in the array. This can be slow
                        if the maximum value is large.

        Parameters:
            - nums (List[int]): A list of integers.
            - threshold (int): The maximum allowed sum of divisions.

        Returns:
            - int: The smallest divisor that satisfies the condition.
    """
    max_val = max(nums)
    # Start checking divisors from 1 up to the maximum element in the array.
    for divisor in range(1, max_val + 2):
        current_sum = 0
        for num in nums:
            current_sum += math.ceil(num / divisor)
        
        if current_sum <= threshold:
            return divisor
    return -1 # Should not be reached given problem constraints

def is_valid_divisor(nums: List[int], divisor: int, threshold: int) -> bool:
    """
        Helper function to check if a given divisor is valid.

        A divisor is considered valid if the sum of the ceiling of each number
        divided by the divisor is less than or equal to the threshold.

        Parameters:
            - nums (List[int]): The list of numbers.
            - divisor (int): The current divisor to check.
            - threshold (int): The maximum allowed sum.

        Returns:
            - bool: True if the divisor is valid, False otherwise. 
    """
    if divisor == 0: # Edge case to prevent division by zero
        return False
        
    div_sum = 0
    for num in nums:
        div_sum += math.ceil(num / divisor)
    
    return div_sum <= threshold

def smallestDivisor(nums: List[int], threshold: int) -> int:
    """
        Finds the smallest divisor using binary search on the answer space.

        The range of possible answers (divisors) is from 1 to the maximum value
        in the input array. We can binary search within this range to efficiently
        find the smallest divisor that satisfies the condition.

        Time Complexity: O(M * log(N)), where M is the number of elements in the
                        array and N is the maximum value in the array. This is
                        significantly more efficient than the brute-force approach.

        Parameters:
            - nums (List[int]): A list of integers.
            - threshold (int): The maximum allowed sum of divisions.

        Returns:
            - int: The smallest divisor that satisfies the condition.
    """
    # The smallest possible divisor is 1, and the largest is max(nums).
    # A divisor larger than max(nums) results in a sum of N, same as divisor=max(nums).
    left, right = 1, max(nums)
    smallest_possible_divisor = right

    while left <= right:
        # Calculate the middle of the current search range.
        mid_divisor = left + (right - left) // 2

        # Check if the mid_divisor is a potential answer.
        if is_valid_divisor(nums, mid_divisor, threshold):
            # If it's a valid divisor, it's a potential answer.
            # We store it and try to find an even smaller divisor.
            smallest_possible_divisor = mid_divisor
            right = mid_divisor - 1
        else:
            # If the sum is too large, we need a larger divisor.
            left = mid_divisor + 1
            
    return smallest_possible_divisor

if __name__ == '__main__':
    print("--- Testing Smallest Divisor Solutions ---")
    
    test_cases = [
        ([1, 2, 5, 9], 6),
        ([2, 3, 5, 7, 11], 11),
        ([19], 5),
        ([44, 22, 33, 11, 55], 5),
        ([1, 1, 1, 1], 4),  # threshold == len(nums)
        ([5, 5, 5, 5], 8),  # equal elements
        ([1000000, 1000000], 3)  # large values, small threshold
    ]

    for i, (arr, thresh) in enumerate(test_cases, 1):
        print(f"\n--- TestCase {i} ---")
        print(f"Input Array: {arr}")
        print(f"Threshold: {thresh}")
        
        # Get results from both functions
        brute_force_result = bruteForce(arr, thresh)
        binary_search_result = smallestDivisor(arr, thresh)
        
        print(f"Brute Force Result: {brute_force_result}")
        print(f"Binary Search Result: {binary_search_result}")
        
        # Verification
        if brute_force_result == binary_search_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")
