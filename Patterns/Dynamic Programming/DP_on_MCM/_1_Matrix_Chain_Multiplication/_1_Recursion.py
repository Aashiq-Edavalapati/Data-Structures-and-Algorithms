"""
    @question:
        Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.
        
        Given an array nums of size n. Dimension of matrix Ai ( 0 < i < n ) is nums[i - 1] x nums[i].Find a minimum number of multiplications needed to multiply the chain.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Examples:
            Input : nums = [10, 15, 20, 25]
            Output : 8000
            Explanation : There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
                        If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.
                        If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
                        Thus minimum number of multiplications required is 8000.

        -------------------------------------------------------------------------------
                        
        Input : nums = [4, 2, 3]
        Output : 24
        Explanation : There is only one way to multiply the chain - A1*A2.
                      Thus minimum number of multiplications required is 24.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

    Constraints:
        2 <= n <= 100
        1 <= nums[i] <= 100
"""
from typing import List

"""
    @intuition:
        Given a matrix chain A1 * A2 * .....Ak....... * An. Let's say we make 1st partition at Ak as 
        (A1 * .. * Ak) * (Ak+1 * ... An). Let's consider it as R1 * R2 => We keep splitting each partition similarly until reach down to a single matrix.
        Currently, after this partitioning, the final operations to multiply R1 * R2, we need p * q * r operations where dimensions of matrices are A1 => p * x, Ak => x * q, An => q * r.

        This gives us the idea that at each step we have to keep track of the current matrices range for which we have to find the minimum operations and the k value at which the optimal partition is found.

"""
def mcm(nums: List[int]) -> int:
    n = len(nums)
    def helper(i: int, j: int) -> int:
        # Base Case: i == j => Chain has a single matrix => 0 operations
        if i == j: return 0
        minOps = float('inf')
        for k in range(i, j):
            # Ai => p * x, Ak => x * q, Aj => q * r:
            #      ops = p * q * r + minops for the chains (Ai * .... * Ak) and (Ak + 1 * ..... * Aj)
            ops = nums[i - 1] * nums[j] * nums[k] + helper(i, k) + helper(k + 1, j)
            minOps = min(minOps, ops)
        
        # Return min ops out of all partitions
        return minOps

    return helper(1, n - 1)

if __name__ == '__main__':
    testCases = [
        [10, 15, 20, 25], # 8000
        [4, 2, 3], # 24
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {mcm(nums)}")