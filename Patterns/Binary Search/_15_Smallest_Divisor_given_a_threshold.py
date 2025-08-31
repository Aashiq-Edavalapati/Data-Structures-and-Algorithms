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
# @pattern: Min. Value that satisfies a given condition
#   - We're not searching *inside* the array; we're searching over possible
#     divisors (1 .. max(nums)).
#   - Monotonicity: As `divisor` increases, each term ceil(num/divisor) is
#     non-increasing, so the total sum is non-increasing. Once the sum becomes
#     ≤ threshold, it stays ≤ for any larger divisor.  → Perfect for
#     "Binary Search on Answer".
#
#   Search space: [1, max(nums)]
#   Feasibility check: is_valid_divisor(nums, d, threshold) → True/False
#
#   Typical pitfalls this solves:
#     * Off-by-one errors in the search space bounds
#     * Using float division instead of integer math; we deliberately use
#       math.ceil(num / d) to match the problem's definition
#
# ------------------------------------------------------------------------------
# @method: Binary Search on Answer
#   1) Define the predicate:
#        is_valid_divisor(nums, d, threshold) :=
#            sum( ceil(num/d) for num in nums ) ≤ threshold
#   2) Because this predicate is monotone in `d`, binary search the smallest `d`
#      that returns True.
#   3) Maintain the invariant:
#        - All divisors in [left, right] are candidates.
#        - When mid is valid, move `right` to mid-1 to find a smaller valid d.
#        - When mid is invalid, move `left` to mid+1 to seek larger divisors.
#
#   Time Complexity:
#     - Brute force:  O(max(nums) * len(nums))
#     - Binary search: O(len(nums) * log(max(nums)))
#   Space Complexity: O(1) extra space for both approaches.
#
#   Edge cases to keep in mind:
#     - threshold < len(nums) → requires divisor > 1 (often much larger)
#     - Very large values in nums
#     - nums contains a single element
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
    # Due to monotonicity, the first divisor that satisfies the constraint is optimal.
    for divisor in range(1, max_val + 2):
        current_sum = 0
        # Compute sum of ceil divisions for this candidate divisor.
        for num in nums:
            # Using math.ceil to honor the problem's rounding rule.
            current_sum += math.ceil(num / divisor)
        
        # If we meet the threshold, we've found the minimal feasible divisor.
        if current_sum <= threshold:
            return divisor
    # Given standard problem constraints, control should return earlier.
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
    # Accumulate ceil(num / divisor) for each element to test feasibility.
    for num in nums:
        div_sum += math.ceil(num / divisor)
    
    # Valid if the sum does not exceed the threshold constraint.
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
    # We keep track of the best (smallest) feasible divisor seen so far.
    smallest_possible_divisor = right

    # Standard lower-bound binary search template.
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
            
    # At loop end, `smallest_possible_divisor` holds the minimal feasible divisor.
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
        
        # Verification: Both methods should agree. If not, re-check predicate
        # monotonicity or search bounds.
        if brute_force_result == binary_search_result:
            print("✅ Results match!")
        else:
            print("❌ Results do NOT match!")
