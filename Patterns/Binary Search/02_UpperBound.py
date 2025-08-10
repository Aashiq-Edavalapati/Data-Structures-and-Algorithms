'''
    @question:
        Find the index(ind) of the smallest element in a sorted array such that arr[ind] > x
'''

def upperBound(arr, x):
    """
        Perform binary search to find the index of the first element strictly greater than x in a sorted array.

        Parameters:
            arr (list): The list of elements (will be sorted inside the function to ensure correctness).
            x (any): The value to compare against.

        Returns:
            int: The index of the first element greater than x.
            Returns -1 if no such element exists.
    """
    # Ensure the array is sorted
    arr = sorted(arr)

    # We use a half-open range [left, right)
    left, right = 0, len(arr)

    # Binary search loop
    while left < right:
        # Midpoint calculation
        mid = left + (right - left) // 2

        if arr[mid] <= x:
            # If arr[mid] is less than or equal to x,
            # the upper bound must be to the right of mid
            left = mid + 1
        else:
            # arr[mid] > x, so this could be our answer
            # but there might be an earlier one, so move right to mid
            right = mid

    # At this point, left == right and points to the first index where arr[left] > x
    if left < len(arr):
        return left  # Index of the first element > x

    # If left is out of bounds, no element > x exists
    return -1


if __name__ == '__main__':
    arr = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]
    x = 11
    print(upperBound(arr, x))  # Output: 9 (arr[9] = 12)
