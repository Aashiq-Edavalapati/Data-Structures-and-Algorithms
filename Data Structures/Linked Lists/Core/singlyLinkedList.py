# Class for Singly Linked List
class SinglyLinkedList: #(SLL)
    # Class representing node: Each node contains data and a pointer pointing to next node.
    class Node:
        # Initializing node with data and next pointer using constructor.
        def __init__(self,data) -> None:
            self.element = data
            self.next = None

    # Constructor for List which initializes the head of the List(representing head node of List) and size of the List(representing no.of Nodes).
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    # Function which returns a boolean value representing whether the List is empty or not.
    def isEmpty(self):
        return self.size == 0
    
    # Function to return the size of the List.
    def getSize(self):
        return self.size
    
    # Function to print the List.
    def printList(self):
        # If the List is empty, then it means there is nothing to print.
        if self.isEmpty():
            raise Exception("List is empty!!!")
        else:
            # Initialize currentNode to head because we have to traverse through the whole list to print value at each node.
            # No matter which node we have to go to we have to start from head, because in SLL nodes are connected in a single way.
            currentNode = self.head
            # If currentNode becomes None(nul), it means that we came to the end of the list. Because SLL ends with a NULL Pointer.
            while currentNode is not None:
                print(currentNode.element,end=" -> ") # Print the currentNode's value
                currentNode = currentNode.next # Update currentNode to it's next Node.
            print("End") # After traversing the whole List print "End".

    # Function to insert a new node at the beggining.
    def insertFirst(self, data):
        newNode = self.Node(data) # Create a newNode with data which is to be inserted.
        newNode.next = self.head # Point next of the newNode to head of the SLL.
        self.head = newNode # Change head of SLL to newNode.
        self.size += 1 # Increase size of the List by 1.

    # Function to insert a new Node at the last of the SLL.
    def insertLast(self,data):
        newNode = self.Node(data) # Create a newNode with data which is to be inserted.
        # If SLL is empty directly make newNode as head.
        if self.isEmpty():
            self.head = newNode
        else:
            currentNode = self.head # Initialize currentNode to head to traverse to the last node of the SLL.
            while currentNode.next != None: # If next of the currentNode is None(null) then it means it is the last node.
                currentNode = currentNode.next # Update currentNode to it's next Node.
            currentNode.next = newNode # Change the next of the last node to the newNode.
        self.size += 1 # Increase the size of the list by 1.
    
    # Function to insert a newNode at a specified position.(Note: I started position from 0, it may vary if you want to start the position counting from 1).
    def insertAtPos(self,data,pos):
        # If position < 0 or position > size of the list: it is not possible, so raise an exception.
        if pos < 0 or pos > self.size:
            raise Exception("Given position is not possible!!")
            return

        newNode = self.Node(data) # Create a newNode with data which is to be inserted.

        # If position is 0, it is same as inserFirst(data).
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            # self.insertFirst(data)
        else:
            currentNode = self.head # Initialize currentNode to head
            currentPos = 0 # Initialize currentPosition to 0.

            while currentPos < pos - 1: # We have to change next of the node before the position in which the newNode is to be inserted as newNode.
                currentNode = currentNode.next # Update currentNode to its next node.
                currentPos += 1 # Increase currentPosition by 1.
            newNode.next = currentNode.next # Once we reach the node before the position in which the newNode is to be inserted. Change the next of newNode as next of that node.
            currentNode.next = newNode # Change the next of the currentNode to newNode.
        self.size += 1 # Increase size of the list by 1.

    
    # Function to delete the first node of the list.
    def deleteFirst(self):
        # If the SLL is empty it means there is nothing to delete.
        if self.isEmpty():
            raise Exception("List is empty, this action cannot be performed!!!")
        else:
            temp = self.head # Temporary node to store head which can be deleted from the memory later.
            self.head = self.head.next # Update head as the 2nd node.
            del temp # Then delete the previous head which is the 1st node for the SLL before updation.
            self.size -= 1 # Decrease the size of the List by 1.

    # Function to delete last node of the list.
    def deleteLast(self):
        # If the SLL is empty it means there is nothing to delete.
        if self.isEmpty():
            raise Exception("List is empty, this operation cannot be performed!!!")
        else:
            # If the next node of the head id NULL, it means there is only 1 element in the list. So make the head of the list as NULL.
            if self.head.next == None:
                temp = self.head # Temporary variable which stores head which is to be deleted after making the head as NULL.
                self.head = None # Make head as NULL.
                del temp # Delete the head of the List(Last Node of the list).
            else:
                currentNode = self.head # Initialize currentNode to head of the SLL.
                # If node next to next of currentNode is NULL, it means that currentNode is 2nd node from last.
                while currentNode.next.next != None:
                    currentNode = currentNode.next # Update currentNode it's next Node.
                # Store the last node int temporary variable so that it can be deleted later.
                temp = currentNode.next 
                currentNode.next = None # Change next of 2nd last node as NULL.
                del temp # DELETE last node which is stored in a temporary variable.
            self.size -= 1 # Decrease size by 1.
    
    def deletePenultimate(self):
        if self.isEmpty():
            raise Exception("List is empty, this operation cannot be performed!!!")

        elif self.head.next is None:
            raise Exception("List has only one node, this operation cannot be performed!!!")

        else:
            if self.head.next.next == None:
                temp = self.head
                self.head = self.head.next
                del temp
            else:
                currentNode = self.head
                while currentNode.next.next.next != None:
                    currentNode = currentNode.next
                temp = currentNode.next
                currentNode.next = currentNode.next.next
                del temp
            self.size -= 1
    
    # Function to delete node at a specific position.
    def deleteAtAPosition(self, position): # Note: here I started position from 1(Not from 0).
        # If head is NULL it means SLL is empty, so throw exception that List is empty.
        if self.head is None:
            raise Exception("List is empty!!")

        # If position < 1 OR position > size, it means given position is invalid.
        if position < 1 or position > self.size:
            raise Exception("Given position is invalid!!")
        
        # If position=1, it is same as deleteFirst.
        if position == 1:
            temp = self.head
            self.head = self.head.next
            del temp
            self.size -= 1
            return

        currentNode = self.head # Initialize currentNode to head.
        # Iterate through list and reach the node before the node at the position we have to delete.
        for _ in range(1,position - 1):
            currentNode = currentNode.next # Change currentNode to it's next node.
        temp = currentNode.next # Store node that is to be deleted in a temporary variable.
        currentNode.next = currentNode.next.next # Change next of currentNode to next of the node that is being deleted.
        del temp # DELETE the required node which is stored in temp.
        self.size -= 1 # Decrease size by 1.


    '''Some extra functions'''    
    def findSize(self): # Describe a recursive algorithm that counts the number of nodes in a singly linked list.
        return self.findSizeHelper(self.head)
    
    def findSizeHelper(self,currNode):
        if currNode is None:
            return 0
        return 1 + self.findSizeHelper(currNode.next)
        

def main():
    sll = SinglyLinkedList()
    sll.insertFirst(10)
    sll.insertFirst(20)
    sll.insertLast(30)
    sll.insertLast(40)
    sll.printList()
    sll.insertAtPos(25, 2)
    sll.printList()
    sll.deleteLast()
    sll.printList() 
    sll.deletePenultimate()
    sll.printList()
    sll.deleteAtAPosition(2)
    sll.printList()
    print(sll.findSize())
    sll.insertFirst(10)
    sll.insertFirst(5)
    sll.insertLast(50)
    sll.insertLast(60)
    sll.printList()


if __name__ == "__main__":
    main()