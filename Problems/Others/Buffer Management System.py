'''
    You are responsible for developing a buffer management system with a fixed-size memory to handle a continuous stream of data efficiently. 
    Implement the following functionalities: 
        • Add Data: Add new data to the fixed-size buffer. When the buffer reaches its maximum capacity, new data should overwrite the oldest data. 
        • Process Data: Remove and process the data from the front of the buffer, updating the buffer to reflect this change. 
    Develop methods to add_data(data) and process_data(). The add_data method should insert new data into the buffer, overwriting the oldest data if 
    the buffer is full. The process_data method should remove and process the data at the front of the buffer and update the buffer accordingly. 
    For example, if the buffer size is 4 and you add data items "1," "2," "3," and "4," and then add another item "5," the system should overwrite "1"
    with "5." Processing the data should remove "2" from the buffer, resulting in the buffer displaying ["3," "4," "5"].
'''


class Buffer:
    class Node:
        def __init__(self,data) -> None:
            self.data = data
            self.next = None
    
    def __init__(self,size) -> None:
        self.head = self.Node(None)
        self.size = max(size,4)
        self.insertionNode = self.head
        currentNode = self.head
        for _ in range(self.size - 1):
            newNode = self.Node(None)
            currentNode.next = newNode
            currentNode = newNode
        currentNode.next = self.head
    
    def add_data(self,data):
        self.insertionNode.data = data
        self.insertionNode = self.insertionNode.next

    def process_data(self):
        if self.insertionNode == self.head and self.head.next.data == None:
            print("Buffer is empty!!")
            return None
        if self.insertionNode.next.data == None:
            data = self.head.data
            self.head.data = None
            self.head = self.head.next
            return data
        data = self.insertionNode.data
        self.insertionNode.data = None
        self.head = self.insertionNode.next
        return data
    
    def printBuffer(self):
        print('[',end='')
        currentNode = self.head
        while currentNode.next != self.head:
            if currentNode.next.data == None:
                break
            print(currentNode.data,end=", ")
            currentNode = currentNode.next
        print(currentNode.data,'\b]')


if __name__ == '__main__':
    buffer = Buffer(4)
    buffer.add_data(1)
    buffer.add_data(2)
    buffer.add_data(3)
    buffer.add_data(4)
    print(buffer.printBuffer())

    buffer.add_data(5)
    print(buffer.printBuffer())

    processed_data = buffer.process_data()
    print(buffer.head.data)
    print(f"Processed data: {processed_data}")
    print(buffer.printBuffer())