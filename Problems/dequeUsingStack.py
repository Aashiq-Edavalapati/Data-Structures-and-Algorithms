class Stack:
    
    # Node class for creating a new node for each element in stack.
    # (class) Node
    class Node:
        # (method) def __init__(
        #     self: Self@Node,
        #     data: Any
        # ) -> None
        # Initializing data and next variables in node class using constructor.
        def __init__(self,data):
            self.data = data
            self.next = None

    # Constructor for stack class, which initializes head denting the current head most element and size representing the current size.
    # (method) def __init__(self: Self@Stack) -> None
    def __init__(self):
        self.head = None
        self.size = 0
    
    # Method which returns a boolean value representing whether stack is empty or not.
    # (method) def isEmpty(self: Self@Stack) -> bool
    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    # Method to push a new element into stack.
    # (method) def push(
    #     self: Self@Stack,
    #     data: Any
    # ) -> None
    def push(self,data):
        newNode = self.Node(data) # Creating a new node with the data that is being pushed into the stack.
        newNode.next = self.head # Changing the next pointer of newNode to current head.
        self.head = newNode # Changing current head to the new Node that have been pushed into the stack now.
        self.size += 1 # Increasing size of the stack by 1 as a new element have been inserted.

    # Method to remove the head most element and return it's value.
    # (method) def pop(self: Self@Stack) -> (Any | None)
    def pop(self):
        # If the stack is empty there is nothing to pop out of the stack.
        if self.isEmpty():
            print("Stack is empty!!")
            return None
        poppedNode = self.head # Temporary variable to store the current head node which is going to popped out of the stack.
        self.head = self.head.next # Changing head to it's next element 
        self.size -= 1 # Decreasing size of the stack by 1 as an element has been popped out of the stack.
        return poppedNode.data # Return the head most element that have been popped out of the stack just now.

    # Method to get the head most element's value without removing it from the stack.
    # (method) def head(self: Self@Stack) -> (Any | None)
    def top(self):
        if self.isEmpty():
            print("Stack is empty!!")
            return None
        else:
            return self.head.data


class Deque:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def enqueueFirst(self,val):
        self.s1.push(val)
    
    def enqueueLast(self,val):
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())
        
        self.s2.push(val)
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())
        
    def dequeueFirst(self):
        return self.s1.pop()
    
    def dequeueLast(self):
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())

        temp = self.s2.pop()
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())
        return temp

    def isEmpty(self):
        return self.s1.isEmpty()
    
    def first(self):
        return self.s1.top()
    
    def last(self):
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())

        temp = self.s2.top()
        while not self.s2.isEmpty():
            self.s1.push(self.s2.pop())
        return temp
