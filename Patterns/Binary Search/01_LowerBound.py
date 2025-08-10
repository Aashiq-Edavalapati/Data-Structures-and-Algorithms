'''
    @question:
        Find the index(ind) of the smallest element in a sorted array such that arr[ind] >= x
'''

def lowerBound(arr, x):
    """
        Perform binary search to find the index of the first element greater than x in a sorted array.

        Parameters:
            arr (list): The list of elements (will be sorted inside the function to ensure correctness).
            x (any): The value to compare against.

        Returns:
            int: The index of the first element greater than x.
            Returns -1 if no such element exists.
    """
    # Ensure the array is sorted
    arr = sorted(arr)

    # left = start of search space
    # right = end of search space (exclusive)
    left, right = 0, len(arr) - 1

    # Loop until search space is empty
    while left < right:
        # Calculate mid-point to avoid overflow in large ranges
        mid = left + (right - left) // 2

        if arr[mid] < x:
            # If the middle element is less than x,
            # then the lower bound must be to the right of mid
            # (exclude mid and everything before it)
            left = mid + 1
        else:
            # If arr[mid] >= x, mid is a potential answer
            # But there might be an even smaller index satisfying the condition
            # So we keep mid in the search space by moving `right` to mid
            right = mid

    # At this point, left == right and points to the first index where arr[left] >= x
    if left < len(arr):
        return left  # Index of the smallest integer >= x

    # If left goes out of bounds, no such element exists
    return -1


# Example usage
if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    print(lowerBound(arr, 9))  # Output: 3  (because arr[3] = 15)
