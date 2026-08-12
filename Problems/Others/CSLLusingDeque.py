class Deque:
    class Node:
        def __init__(self,val) -> None:
            self.val = val
            self.next = None
            self.prev = None
        
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.sz = 0

    def isEmpty(self):
        return self.sz == 0
    
    def size(self):
        return self.sz
    
    def first(self):
        if self.isEmpty():
            return "Deque is Empty"
        
        return self.head.val
    
    def last(self):
        if self.isEmpty():
            return "Deque is Empty"
        
        return self.tail.val
    
    def enqueueFirst(self, val):
        newNode = self.Node(val)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.sz += 1
    
    def enqueueLast(self, val):
        newNode = self.Node(val)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.sz += 1
    
    def dequeueLast(self):
        if self.isEmpty():
            return "Deque is empty!!"
        
        if self.head == self.tail:
            temp = self.tail.val
            self.head = self.tail = None
            self.sz -= 1
            return temp
        temp = self.tail.val
        self.tail = self.tail.prev
        self.sz -= 1
        return temp
    
    def dequeueFirst(self):
        if self.isEmpty():
            return "Deque is Empty!!"
        
        if self.head == self.tail:
            temp = self.head.val
            self.head = self.tail = None
            self.sz -= 1
            return temp
        
        temp = self.head.val
        self.head = self.head.next
        self.sz -= 1
        return temp
    

class CircularSinglyLinkedList:
    def __init__(self) -> None:
        self.sll = Deque()
    
    def first(self):
        return self.sll.first()
    
    def last(self):
        return self.sll.last()
    
    def isEmpty(self):
        return self.sll.isEmpty()
    
    def insertFirst(self,val):
        self.sll.enqueueFirst(val)
        self.sll.tail.next = self.sll.head
    
    def insertLast(self,val):
        self.sll.enqueueLast(val)
        self.sll.tail.next = self.sll.head
    
    def deleteFirst(self):
        if self.sll.isEmpty():
            return "List is empty!!"
        
        d = self.sll.dequeueFirst()
        if not self.sll.isEmpty():
            self.sll.tail.next = self.sll.head
        return d
    
    def deleteLast(self):
        if self.sll.isEmpty():
            return "List is empty!!"
        
        d = self.sll.dequeueLast()
        if not self.sll.isEmpty():
            self.sll.tail.next = self.sll.head
        return d
    


# Driver code to test CircularSinglyLinkedList

if __name__ == "__main__":
    # Initialize the circular singly linked list
    csll = CircularSinglyLinkedList()

    # Test isEmpty on an empty list
    print("Is list empty?", csll.isEmpty())  # Expected: True

    # Insert elements
    print("\nInserting elements at the end:")
    csll.insertLast(10)
    print("First element:", csll.first())  # Expected: 10
    print("Last element:", csll.last())    # Expected: 10
    csll.insertLast(20)
    print("First element:", csll.first())  # Expected: 10
    print("Last element:", csll.last())    # Expected: 20
    csll.insertLast(30)
    print("First element:", csll.first())  # Expected: 10
    print("Last element:", csll.last())    # Expected: 30

    # Insert element at the front
    print("\nInserting elements at the front:")
    csll.insertFirst(5)
    print("First element:", csll.first())  # Expected: 5
    print("Last element:", csll.last())    # Expected: 30
    csll.insertFirst(0)
    print("First element:", csll.first())  # Expected: 0
    print("Last element:", csll.last())    # Expected: 30

    # Test circular nature by checking if tail's next points to head
    print("\nChecking circular property:")
    print("Tail's next points to:", csll.sll.tail.next.val)  # Expected: First element (0)

    # Delete elements from the front
    print("\nDeleting elements from the front:")
    print("Deleted:", csll.deleteFirst())  # Expected: 0
    print("First element:", csll.first())  # Expected: 5
    print("Deleted:", csll.deleteFirst())  # Expected: 5
    print("First element:", csll.first())  # Expected: 10
    print("Deleted:", csll.deleteFirst())  # Expected: 10
    print("First element:", csll.first())  # Expected: 20

    # Delete elements from the end
    print("\nDeleting elements from the end:")
    print("Deleted:", csll.deleteLast())   # Expected: 30
    print("First element:", csll.first())  # Expected: 20
    print("Deleted:", csll.deleteLast())   # Expected: 20
    print("Is list empty?", csll.isEmpty())  # Expected: True

    # Try to delete from an empty list
    print("\nAttempt to delete from an empty list:")
    print("Deleted first:", csll.deleteFirst())  # Expected: "List is empty!!"
    print("Deleted last:", csll.deleteLast())    # Expected: "List is empty!!"

    
