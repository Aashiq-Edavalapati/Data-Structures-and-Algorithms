# Time Complexity:                                  Space Complexity:
#       Best Case  : O(nlogn)                              Best Case  : O(n)
#       AVG. Case  : O(nlogn)                              AVG. Case  : O(n)
#       Worst Case : O(nlogn)                              Worst Case : O(n)

# Stable, Not adaptive, non-linear, Recursive.


def mergeSort(arr):
    # There is only one element means it is already sorted. So, return it.
    if len(arr) == 1:
        return arr

    mid = (len(arr) - 1) // 2
    # Split array into 2 halves and sort each half seperately using recursive call and merge function.
    left = mergeSort(arr[:mid + 1]) # Sort left half
    right = mergeSort(arr[mid + 1:]) # Sort right half

    return merge(left,right) # Merge back the sorted subarrays to form a single sorted subarray in each recursive
                             # call and into a single sorted array at last.

def merge(arr1,arr2):
    i = 0  # Pointer for keeping track of traversal of arr1(left).
    j = 0  # Pointer for keeping track of traversal of arr2(right).
    merged = []
    
    # Merge the two sorted subarrays using two pointers till either of the pointers reaches end of the subarray.
    while i < len(arr1) and j < len(arr2):
        # if current element in left subarray < current element of right subarray => arr1[i] is <=  every
        # other element > current in both left and right subarrays. Because, each of them is sorted individually. 
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1 # Move i to next position.
        else:
            merged.append(arr2[j])
            j += 1 # Move j to next position.

    # When j reaches end of the subarray right but there are elements left in left subarray.
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    # When i reaches end of the subarray left but there are elements left in right subarray.
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged # Return merged subarray.