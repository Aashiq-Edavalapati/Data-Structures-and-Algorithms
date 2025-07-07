# Time Complexity:                                  Space Complexity:
#       Best Case  : O(nlogn)                              Best Case  : O(1)
#       AVG. Case  : O(nlogn)                              AVG. Case  : O(1)
#       Worst Case : O(nlogn)                              Worst Case : O(1)

# Stable, Not adaptive, non-linear, Recursive.

class QuickSortInPlace:
    # Constructor to initialize the input array into this class.
    def __init__(self, arr) -> None:
        # intializing the array.
        self.arr = arr
    
    def sort(self):
        self.quickSortInPlace(self.arr, 0, len(self.arr) - 1)

    def quickSortInPlace(self, arr, low, high):
        # Base case for the following recursive function is when low = high.
        # Check if low < high because if low >= high, that means there is no upperbound.
        if low < high:
            # Get pivot index after completing one partitioning. Because, we have to know where the array is 
            # partitioned so that we can perform quicksort on those partitions.
            pivotIndex = self.partition(arr,low,high)

            # Recursive call to sort left partition of the pivot.
            self.quickSortInPlace(arr, low, pivotIndex - 1)

            #Recursive call to sort the right partition of the pivot.
            self.quickSortInPlace(arr, pivotIndex + 1, high)
    
    def partition(self, arr, low, high):
        # Choose last element in the partition as pivot element.
        pivot = arr[high]

        # Pointer to keep track of where the pivot finally should be and bring all the elements smaller than 
        # pivot to the start of the partition.
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                # Increment i, because we have to swap the smaller element with the 
                i += 1

                # Swap current element with element at position i.
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap pivot element with the first element in the partition that is greater than pivot.
        arr[high], arr[i + 1] = arr[i + 1], arr[high]

        # This will return the index of pivot after arranging all the numbers smaller than pivot on left side of 
        # the pivot and all the elements greater than the pivot on the right side of the pivot
        return i + 1
    

def main():
    arr = list(map(int, input("Enter the elements of array: ").split()))
    obj = QuickSortInPlace(arr)
    obj.sort()
    print("Sorted array using in-place quick sort is: ",arr)

if __name__ =='__main__':
    main()