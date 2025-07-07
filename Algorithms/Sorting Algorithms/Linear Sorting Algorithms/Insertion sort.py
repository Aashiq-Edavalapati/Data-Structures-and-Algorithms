# Time Complexity:
#       Best Case : O(n)
#       AVG. Case : O(n^2)
#       Worst Case : O(n^2)

# Stable, in-place, adaptible.


def insertionSort(arr):
    # Do (n - 1) iterations from 1 to (n - 1).
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        # So, that key will be taken to its correct position in that subarray.
        while j >= 0 and key < arr[j]: # Note that the subarray before the arr[i] is already sorted!
            arr[j + 1] = arr[j]
            j -= 1

        # Inserting key into it's correct position in sorted subarray.
        arr[j + 1] = key