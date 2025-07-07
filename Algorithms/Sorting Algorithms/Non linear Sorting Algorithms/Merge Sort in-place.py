# Time Complexity:                                  Space Complexity:
#       Best Case  : O(nlogn)                              Best Case  : O(1)
#       AVG. Case  : O(nlogn)                              AVG. Case  : O(1)
#       Worst Case : O(nlogn)                              Worst Case : O(1)

# Stable, Not adaptive, non-linear, Recursive.

def merge_sort_in_place(arr, l, r):
    # if l = r, it means that the size of the subarray is 1 which means it is already sorted and no more halvings
    # required. Similarly l > r means r has become -ve in case of left subarray and l has crossed array size in 
    # cas of right subarray.
    if l < r:
        # Same as (l + r) // 2, but avoids overflow for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m) # Left half
        merge_sort_in_place(arr, m + 1, r) # Right half

        merge(arr, l, m, r)


def merge(arr, start, mid, end):
    start2 = mid + 1

    # If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1 and element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1