# Time Complexity:
#       Best Case : O(n^2)
#       AVG. Case : O(n^2)
#       Worst Case : O(n^2)

# Not Stable, in-place, not adaptible.

def selectionSort(arr):
    # Loop (n - 1) times. Not n times because, after finding all the min's till n-1th iteration the only element 
    # left is the last element.
    for i in range(len(arr) - 1):
        min_ind = i

        # Find min element in the unsorted portion.
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        # Swap min element with first element of the current unsorted portion.
        arr[i], arr[min_ind] =arr[min_ind], arr[i]