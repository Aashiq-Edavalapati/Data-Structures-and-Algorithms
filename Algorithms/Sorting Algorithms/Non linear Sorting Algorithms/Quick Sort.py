# Time Complexity:                                  Space Complexity:
#       Best Case  : O(nlogn)                              Best Case  : O(n)
#       AVG. Case  : O(nlogn)                              AVG. Case  : O(n)
#       Worst Case : O(n^2)                                Worst Case : O(n)
    #         |
    #         |
    #         v  
      # (occurs when the smallest or largest element is always chosen as the pivot, such as in a sorted array)


# Stable, Not adaptive, non-linear, Recursive.

def quickSort(arr):
    # if length of array is <= 1 it means array is already sorted.
    if len(arr) <= 1:
        return arr
    
    # Let us take pivot as the last element.
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot] # Contains all the elements < pivot
    right = [x for x in arr[:-1] if x >= pivot] # Contains all the elements >= pivot

    # Return sorted(left) subarray + pivot + sorted(right) subarray.
    return quickSort(left) + [pivot] + quickSort(right)


# Driver Code
my_list = [3,7, 8, 5, 2, 1, 9, 6, 4]
sorted_list = quickSort(my_list)
print(sorted_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)