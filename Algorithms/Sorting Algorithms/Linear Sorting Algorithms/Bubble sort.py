# Time Complexity:
#       Best Case  : O(n)
#       AVG. Case  : O(n^2)
#       Worst Case : O(n^2)

# Stable, in-place, adaptible.


def bubbleSort(arr):
    # Do (n - 1) iterations. In each iteration max element is taken to end of the unsorted subarray.
    for i in range(len(arr) - 1):
        swapped = False
        # Take largest element to the end of the unsorted subarray.
        for j in range(len(arr) - i - 1):
            # If current element is greater than next element swap those two.
            if arr[j] > arr[j + 1]:
                swapped = True # As swap is going to take place change swapped to True.
                arr[j + 1], arr[j] = arr[j], arr[j + 1] # Swap current and next elements.
        
        # If no swap took place in the current iteration, it means that the array is already sorted.
        # So break out of the loop.
        if not swapped:
            return