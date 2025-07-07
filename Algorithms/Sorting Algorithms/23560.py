''' 
    In this lab session I have learnt how to implement in place quick sort using recursion. I have understood the process of implementation of it.
    I have learnt that from GFG, HackerRank with a visual representation of the process. Instead of creating a new list of each partition every time,
    in in-place quick sort we use pointers to keep track of current pivot index to perform quicksort on the partition left and right of the pivot & low, high 
    pointers to know the partition in which we are going to perform quick sort next. I have created a class to define the implementation of in-place quick sort
    and a driver program which tests the implementation by giving some sample inputs.


    Souces: GPT, GFG, HackerRank.

    I have also discussed in-place merge sort with my neighbor classmate and implemented it also.
'''




class QuickSortInPlace:
    #     (method) def quickSortInPlace(
    #     self: Self@QuickSortInPlace,
    #     arr: Any,
    #     low: Any,
    #     high: Any
    # ) -> None

    # Constructor to initialize the input array into this class.
    def __init__(self, arr) -> None:
        # intializing thearray.
        self.arr = arr
    
    def sort(self):
        self.quickSortInPlace(self.arr, 0, len(self.arr) - 1)

    def quickSortInPlace(self, arr, low, high):
        # Base case for the following recursive function is when low = high.
        # Check if low < high because if low >= high, that means there is no upperbound.
        # (parameter) high: Any
        if low < high:
            # Get pivot index after completing one partitioning. Because, we have to know where the array is partitioned so that we can perform quicksort on those partitions.
            # (variable) pivotIndex: Any
            pivotIndex = self.partition(arr,low,high)

            # Recursive call to sort left partition of the pivot.
            # (method) def quickSortInPlace(
            #     arr: Any,
            #     low: Any,
            #     high: Any
            # ) -> None
            self.quickSortInPlace(arr, low, pivotIndex - 1)

            #Recursive call to sort the right partition of the pivot.
            # (method) def quickSortInPlace(
            #     arr: Any,
            #     low: Any,
            #     high: Any
            # ) -> None
            self.quickSortInPlace(arr, pivotIndex + 1, high)
    
    # (method) def partition(
    #     self: Self@QuickSortInPlace,
    #     arr: Any,
    #     low: Any,
    #     high: Any
    # ) -> Any
    def partition(self, arr, low, high):
        # Choose last element in the partition as pivot element.
        # (variable) pivot: Any
        pivot = arr[high]

        # Pointer to keep track of where the pivot finally should be and bring all the elements smaller than pivot to the start of the partition.
        # (variable) i: Any
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                # Increment i, because we have to swap the smaller element with the 
                i += 1

                # Swap current element with element at position i.
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap pivot element with the first element in the partition that is greater than pivot.
        arr[high], arr[i + 1] = arr[i + 1], arr[high]

        # This will the index of pivot after arranging all the numbers smaller than pivot on left side of the pivot and all the elements greater than the pivot on the right side of the pivot
        return i + 1
    

class InPlaceMergeSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self._merge_sort(0, len(self.array) - 1)

    def _merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2

            # Recursively sort both halves
            self._merge_sort(left, mid)
            self._merge_sort(mid + 1, right)

            # Merge the sorted halves
            self._in_place_merge(left, mid, right)

    def _in_place_merge(self, left, mid, right):
        start2 = mid + 1

        # If the direct merge is already sorted
        if self.array[mid] <= self.array[start2]:
            return

        while left <= mid and start2 <= right:
            if self.array[left] <= self.array[start2]:
                left += 1
            else:
                value = self.array[start2]
                index = start2

                # Shift all elements between left and start2 to the right
                while index != left:
                    self.array[index] = self.array[index - 1]
                    index -= 1
                self.array[left] = value

                # Update all pointers
                left += 1
                mid += 1
                start2 += 1

    def get_sorted_array(self):
        return self.array

# (function) def main() -> None
def main():
    arr = list(map(int, input("Enter the elements of array: ").split()))
    arr1 = arr.copy()
    obj = QuickSortInPlace(arr)
    obj.sort()
    print("Sorted array using in-place quick sort is: ",arr)

    array = [12, 11, 13, 5, 6, 7]

    # Create an instance of InPlaceMergeSort
    sorter = InPlaceMergeSort(array)
    
    # Perform the sort
    sorter.sort()
    
    # Retrieve and print the sorted array
    sorted_array = sorter.get_sorted_array()
    print("Sorted array using merge sort is:", sorted_array)

     

if __name__ == '__main__':
    main()