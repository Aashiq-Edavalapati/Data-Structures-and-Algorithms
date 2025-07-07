# Stack implementation using singly linked list.
# Source: ChatGPT
# The query that I have asked GPT is: I pasted my code in it and asked whether the implementation is correct. And took a small help for reading input from a file



# (class) Stack
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


if __name__ == '__main__':
    stack = Stack()
    
    x = open("stackInput.txt",'r')
    operations = x.readlines()
    for i in range(len(operations) - 1):
        operations[i] = operations[i][:-1].strip().lower()
    for operation in operations:
        if operation == 'p':
            stack.pop()
        elif operation[0] == 'p':
            stack.push(int(operation[3:]))
        elif operation == 't':
            print(stack.top())
        elif operation == 's':
            print(stack.getSize())
        elif operation == 'i':
            print(stack.isEmpty())
        else:
            continue