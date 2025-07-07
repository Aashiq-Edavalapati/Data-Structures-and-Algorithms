class BinaryMaxHeap:
    def __init__(self) -> None:
        self.heapList = [0] # List to store elements of heap
        self.sz = 0
    
    def upHeap(self,i): # O(log(n))
        """
            Upheap the element at a given index in the heapList to restore heap order property.
        """
        # if i // 2 = 0, it means we are at the root.
        # if i // 2 < 0, it means given index is not valid.
        while i//2 > 0:
            # if currentElement < parent, swap these 2 pushing current element to the above layer.
            if self.heapList[i] > self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i //= 2

    def insert(self,val): # O(log(n))
        """
            Inserts a new element and upheap it to take it to correct position.
        """
        # Insert new element as we insert into a complete BT(i.e., at the rightmost position).
        self.heapList.append(val)
        self.sz += 1 
        self.upHeap(self.sz) # Perform upheap on the inserted element to restore heap order property
    
    def maxChild(self,i): # O(1)
        """
            Returns the index of minimum child of a given element
        """
        # If there is no left child for given node => no children
        if 2 * i > self.sz:
            return "There are no children for the given element"

        # If there is no right child return left child.
        if 2 * i + 1 > self.sz:
            return i * 2
        
        # Otherwise, return minimum of right and left children.
        return i * 2 if self.heapList[i * 2] > self.heapList[i * 2 + 1] else i * 2 + 1

    def downHeap(self,i): # O(log(n))
        """
            Downheaps the given element in the heap. (Restores heap order property)
        """
        # check only till children exist
        while i * 2 <= self.sz:
            mc = self.maxChild(i) # Get maxChild to swap it with the current element if we have to
            if self.heapList[i] < self.heapList[mc]: # Swap current element with maxChild if it is greater than maxChild
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
                i = mc
            else:
                break

    def delMax(self): # O(log(n))
        """
            Deletes minimum element(Basically, root) in the heap and returns it. 
        """
        if self.sz == 0:
            return "Heap is empty!!"
        
        minElement = self.heapList[1]
        last = self.heapList.pop()
        self.heapList[1] = last # Replace root with rightmost leaf in last level.
        self.sz -= 1 
        self.downHeap(1) # DownHeap the new root to restore heap order property
        return minElement

    def buildHeap(self,eltList): # O(nlog(n))
        """
            Builds heap from an input list.
        """
        for element in eltList:
            self.insert(element)


    def bottomUpBuilding(self,eltList): # O(nlog(n))
        """
            Bottom-up heap construction from an unordered list.
        """
        self.sz = len(eltList)
        self.heapList = [0] + eltList[:]  # Copy the list to the heap (0 is a placeholder for easier index calculations)

        # Start from the last non-leaf node and downheap each node up to root
        i = self.sz // 2
        while i > 0:
            self.downHeap(i)
            i -= 1

    def heapify(self, bt): # O(log(n))
        """
            Heapifies a given Binary Tree.
        """
        self.sz = len(bt)  # Set size to the length of the list
        self.heapList = [0] + bt[:]  # Copy the list to the heap (0 is a placeholder for easier index calculations)
        
        # Start at the last non-leaf node and perform downHeap on each node up to the root
        i = self.sz // 2
        while i > 0:
            self.downHeap(i)
            i -= 1

if __name__ == '__main__':
    heap = BinaryMaxHeap()
    eltList = [5,2,1,3,7,6,8,9,10,23,20,15,16]
    heap.buildHeap(eltList)
    print(heap.heapList)
    heap.delMax()
    heap.delMax()
    print(heap.heapList)