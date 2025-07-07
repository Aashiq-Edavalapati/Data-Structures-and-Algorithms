class deque:
    class Node:
        def __init__(self,data) -> None:
            self.data = data
            self.next = None
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.sz = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def size(self):
        return self.sz
    
    def first(self):
        return self.head.data
    
    def last(self):
        return self.tail.data
    
    def enqueueFirst(self, data):
        if self.head is None:
            self.head = self.Node(data)
            self.tail = self.head
        
        else:
            newNode = self.Node(data)
            newNode.next = self.head
            self.head = newNode
        self.sz += 1

    def enqueueLast(self, data):
        if self.head is None:
            self.head = self.Node(data)
            self.tail = self.head

        else:
            self.tail.next = self.Node(data)
        self.sz += 1
    
    def dequeueFirst(self):
        if self.head is None:
            print("Deque is Empty!!")
            return
        
        if self.head.next is None:
            temp = self.head.data
            self.head.next = None
            self.tail = None
            self.sz -= 1
            return temp
        
        else:
            temp = self.head
            self.head = self.head.next
            self.sz -= 1
            return temp.data
        
    def dequeueLast(self):
        if self.head is None:
            print("Deque is Empty!!")
            return
        current = self.head
        while current.next != self.tail:
            current = current.next

        value = self.tail.data
        self.tail = current
        self.tail.next = None
        self.sz -= 1
        return value


