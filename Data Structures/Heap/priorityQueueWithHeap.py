from heap import BinaryMinHeap

"""
    Preamble:
        Class Signature:
            (class) PriorityQueue

        This class represents a priority queue implemented using a binary min-heap.
        Each element in the queue is stored as a key-value pair, where the key represents
        the priority, and the object represents the associated value.

        Parameters:
            1) heap : BinaryMinHeap --> A binary min-heap to store the elements of the priority queue.

        Methods:
            1) (method) def insertItem(self: Self@PriorityQueue, k: Any, o: Any) -> None :- 
                Inserts a new item into the priority queue with a specified key (priority) `k` and object `o`, 
                and ensures that the heap property is maintained.

            2) (method) def removeMin(self: Self@PriorityQueue) -> Tuple :- 
                Removes and returns the key-value pair with the smallest key (highest priority) from the priority queue.

            3) (method) def minKey(self: Self@PriorityQueue) -> Any :- 
                Returns the smallest key (highest priority) in the priority queue without removing it.

            4) (method) def minElement(self: Self@PriorityQueue) -> Any :- 
                Returns the object with the smallest key (highest priority) in the priority queue without removing it.

            5) (method) def size(self: Self@PriorityQueue) -> int :- 
                Returns the current number of elements in the priority queue.

            6) (method) def isEmpty(self: Self@PriorityQueue) -> bool :- 
                Returns True if the priority queue is empty, otherwise returns False.
"""
class PriorityQueue:
    def __init__(self):
        # Using a BinaryMinHeap to store (key, value) tuples
        self.heap = BinaryMinHeap()

    def insertItem(self, k, o):
        """
        Inserts a new item into the priority queue with key `k` and object `o`.
        """
        # Insert the tuple (k, o) into the min heap
        self.heap.insert((k, o))

    def removeMin(self):
        """
        Removes and returns the item with the smallest key in the priority queue.
        """
        if self.isEmpty():
            return "Priority Queue is empty"
        # The min element is at the root, remove it using delMin from BinaryMinHeap
        return self.heap.delMin()

    def minKey(self):
        """
        Returns the smallest key in the priority queue without removing it.
        """
        if self.isEmpty():
            return "Priority Queue is empty"
        # The root element has the smallest key
        return self.heap.heapList[1][0]

    def minElement(self):
        """
        Returns the object with the smallest key in the priority queue without removing it.
        """
        if self.isEmpty():
            return "Priority Queue is empty"
        # The root element has the smallest key, return the object
        return self.heap.heapList[1][1]

    def size(self):
        """
        Returns the size of the priority queue.
        """
        return self.heap.sz

    def isEmpty(self):
        """
        Returns True if the priority queue is empty, False otherwise.
        """
        return self.heap.sz == 0


# Test the PriorityQueue implementation
if __name__ == '__main__':
    pq = PriorityQueue()
    
    # Insert some items into the priority queue
    pq.insertItem(5, 'A')
    pq.insertItem(9, 'C')
    pq.insertItem(3, 'B')
    pq.insertItem(7, 'D')
    print(pq.minElement())
    print(pq.minKey())
    print(pq.removeMin())
    print(pq.minElement())
    print(pq.removeMin())
    print(pq.removeMin())

