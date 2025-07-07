class CircularLinkedList:
    class Node:
        def __init__(self,data) -> None:
            self.element = data
            self.next = None
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def printList(self):
        if self.isEmpty():
            print("List is empty!!")
        
        else:
            currentNode = self.head
            while currentNode.next != self.head:
                print(currentNode.element, end="->")
                currentNode = currentNode.next
            print(self.head.element)

    def insert_At_first(self,data):
        new_node = self.Node(data)
        if(self.size == 0):
            self.head = new_node
            self.head.next = self.head
        else:
            current_node = self.head
            while(current_node.next != self.head):
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
            self.head = new_node
            
        self.size+=1

    def insert_at_last(self,data):
        new_node = self.Node(data)
        if(self.size == 0):
            self.head = new_node
            self.head.next = new_node
        else:
            current_node = self.head
            while(current_node.next != self.head):
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
        self.size+=1

    def insert_at_a_pos(self,data,pos):
        new_node = self.Node(data)
        if pos<0 or pos>self.size:
            print("Not possible")
            return
        if pos == 0:
            if self.isEmpty():
                self.head = new_node
                self.head.next = self.head
                self.size+=1
                return
            new_node.next = self.head
            current_node = self.head
            while(current_node.next != self.head):
                current_node = current_node.next
            current_node.next = new_node
            self.head = new_node
            self.size+=1
            return
        current_node = self.head
        for i in range(pos-1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        self.size+=1
    
    def deleteFirst(self):
        if self.isEmpty():
            print("The list is empty!! Cannot perform this operation!")
            return
        if self.head.next == None:
            self.head = None
            self.size -= 1
            return
        currentNode = self.head
        while currentNode.next != self.head:
            currentNode = currentNode.next
        currentNode.next = self.head.next
        temp = self.head
        self.head = self.head.next
        del temp
        self.size -= 1

    def deleteLast(self):
        if self.isEmpty():
            print("List is empty! Cannot perform this operation!!!")
            return
        if self.head.next == None:
            self.head = None
            self.size -= 1
            return

        currentNode = self.head
        while currentNode.next.next != self.head:
            currentNode = currentNode.next
        temp = currentNode.next
        currentNode.next = self.head
        del temp
        self.size -= 1

    
