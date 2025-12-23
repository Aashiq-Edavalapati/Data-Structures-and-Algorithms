# Class for Doubly Linked List.
class DoublyLinkedList:
    # Nested class representing a node in the doubly linked list.
    class Node:
        # Consturctor for Node class.
        def __init__(self, data) -> None:
            # Each node contains a reference to the previous node, its data, and the next node.
            self.previous = None
            self.element = data
            self.next = None
    
    # Constructor for DLL class.
    def __init__(self) -> None:
        # The doubly linked list starts with no head node and a size of 0.(initially)
        self.head = None
        self.size = 0

    # Method to check if the list is empty.
    def isEmpty(self):
        return self.size == 0
    
    # Method to get the current size of the list.
    def getSize(self):
        return self.size
    
    # Method to print all elements in the list.
    def printList(self):
        currentNode = self.head
        # Traverse the list and print each element.
        while currentNode is not None:
            print(currentNode.element, end=" <--> ")
            currentNode = currentNode.next # Update currentNode to it's next Node.
        print("THE END!!")
    
    # Method to insert a new element at the beginning of the list.
    def insertFirst(self, data):
        newNode = self.Node(data)  # Create a new node with the given data.
        if self.isEmpty():  # If the list is empty, make the new node as the head.
            self.head = newNode 
        else: # Otherwise, insert the new node before the current head.
            newNode.next = self.head # Change next of newNode to current head.
            self.head.previous = newNode # Change previous of current head from NULL to newNode.
            self.head = newNode # Change the head as newNode.
        self.size += 1  # Increment the size of the list.

    # Method to insert a new element at the end of the list.
    def insertLast(self, data):
        newNode = self.Node(data)  # Create a new node with the given data.
        if self.isEmpty():  # If the list is empty, make the new node the head.
            self.head = newNode
        else:
            # Traverse to the end of the list.
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            # Insert the new node after the last node.
            newNode.previous = currentNode
            currentNode.next = newNode
        self.size += 1  # Increment the size of the list.

    # Method to insert a new element at a specific position in the list.
    def insertAtPos(self, data, pos):
        if pos < 0 or pos > self.size:  # Check if the position is valid.
            print("Given position is invalid!!!")
            return

        newNode = self.Node(data)  # Create a new node with the given data.

        if pos == 0:  # If the position is 0, insert at the beginning.
            self.insertFirst(data)
        else:
            currentPos = 0
            currentNode = self.head
            # Traverse to the position just before the insertion point.
            while currentPos < pos - 1:
                currentNode = currentNode.next
                currentPos += 1
            # Insert the new node at the specified position.
            newNode.previous = currentNode
            newNode.next = currentNode.next
            if currentNode.next is not None:
                currentNode.next.previous = newNode
            currentNode.next = newNode
        self.size += 1  # Increment the size of the list.
    
    # Method to delete the first element in the list.
    def deleteFirst(self):
        if self.isEmpty():  # If the list is empty, print a message.
            print("The list is empty, we cannot perform this operation")
        else:
            if self.head.next == None:  # If there's only one element, remove it.
                self.head = None
            else:
                # Otherwise, remove the first element and update the head.
                self.head.next.previous = None
                temp = self.head
                self.head = self.head.next
                del temp  # Free the memory of the old head.
            self.size -= 1  # Decrement the size of the list.
        
    # Method to delete the last element in the list.
    def deleteLast(self):
        if self.isEmpty():  # If the list is empty, print a message.
            print("List is empty, cannot perform this operation!!!")
        else:
            if self.head.next == None:  # If there's only one element, remove it.
                self.head = None
            else:
                # Otherwise, traverse to the last element and remove it.
                currentNode = self.head
                while currentNode.next != None:
                    currentNode = currentNode.next
                currentNode.previous.next = None
                del currentNode  # Free the memory of the last node.
            self.size -= 1  # Decrement the size of the list.
        
    # Method to delete the penultimate (second-to-last) element in the list.
    def deletePenultimate(self):
        if self.isEmpty():  # If the list is empty, print a message.
            print("List is empty, cannot perform the specified operation!!!")
            return
        
        if self.head.next == None:  # If there's only one element, print a message.
            print("There is only one element!!")
            return
        
        if self.head.next.next == None:  # If there are only two elements, remove the first.
            temp = self.head
            self.head = self.head.next
            self.head.previous = None
            del temp  # Free the memory of the old head.
            self.size -= 1
            return

        # Otherwise, traverse to the penultimate element and remove it.
        currentNode = self.head
        while currentNode.next.next != None:
            currentNode = currentNode.next
        
        temp = currentNode
        currentNode.previous.next = currentNode.next
        currentNode.next.previous = currentNode.previous
        del temp  # Free the memory of the penultimate node.
        self.size -= 1  # Decrement the size of the list.


# Driver function to test the Doubly Linked List.
def driver():
    dll = DoublyLinkedList()  # Create a new doubly linked list.
    
    print("Insert elements at the beginning:")
    dll.insertFirst(10)  # Insert 10 at the beginning.
    dll.insertFirst(20)  # Insert 20 at the beginning.
    dll.insertFirst(30)  # Insert 30 at the beginning.
    dll.printList()  # Expected: 30, 20, 10, THE END!!
    
    print("Insert elements at the end:")
    dll.insertLast(40)  # Insert 40 at the end.
    dll.insertLast(50)  # Insert 50 at the end.
    dll.printList()  # Expected: 30, 20, 10, 40, 50, THE END!!
    
    print("Insert element at position 2:")
    dll.insertAtPos(25, 2)  # Insert 25 at position 2.
    dll.printList()  # Expected: 30, 20, 25, 10, 40, 50, THE END!!
    
    print("Delete the first element:")
    dll.deleteFirst()  # Delete the first element
    dll.printList()  # Expected: 20, 25, 10, 40, 50, THE END!!
    
    print("Delete the last element:")
    dll.deleteLast()  # Delete the last element
    dll.printList()  # Expected: 20, 25, 10, 40, THE END!!
    
    print("Delete the penultimate element:")
    dll.deletePenultimate()  # Delete the second-to-last element
    dll.printList()  # Expected: 20, 25, 40, THE END!!
    
    print("Current size of the list:", dll.getSize())  # Expected: 3


# Execute the driver function if this script is run directly
if __name__ == '__main__':
    driver()
