# Implementation of binary search algorithm in Python
def binary_search(arr, target):
    """
        Perform binary search on a sorted array.

        Parameters:
            arr (list): Sorted list of elements to search.
            target (any): Element to search for.

        Returns:
            int: Index of target if found, else -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate mid and prevent overflow

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1

# Example usage:
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in array")