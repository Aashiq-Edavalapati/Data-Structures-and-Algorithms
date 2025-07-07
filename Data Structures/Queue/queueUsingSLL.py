

# A linked list node
class Node:
    # Constructor for Node class
    def __init__(self, key, next=None):
        self.data = key
        self.next = next
 
 
class Queue:
    # Constructor for Queue
    def __init__(self):
        self.fnt = None
        self.rear = None
        self.sz = 0
 
    # Function to add a new element next to rear
    def enqueue(self, x):
        newNode = Node(x) # Create a new Node
        if self.isEmpty():
            self.fnt = newNode
            self.rear = self.fnt
            self.sz += 1
            return
        
        self.rear.next = newNode
        self.rear = newNode
        self.sz += 1

    # Dequeue function to remove the top element(i.e, First element that is inserted into the queue)
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!!")
            return
        itemDeleted = self.fnt
        self.fnt = self.fnt.next
        self.sz -= 1
        return itemDeleted.data

    # Function that returns a boolean value representing whether Queue is empty or not
    def isEmpty(self):
        return self.sz == 0
 
    # Function to return top element in a Queue
    def front(self):
        return self.fnt.data

    # Function to return size of the Queue
    def size(self):
        return self.sz

    # Function to print the Queue
    def printQueue(self):
        tnode = self.fnt
        while tnode!=None:
            print(tnode.data,end=" ")
            tnode = tnode.next
        print("")
        return
    
 
 

# Driver code.---------------------------------------------

def testQueue(op, d):
    #testcases=int(input())
    #stacksize=int(input())
    Qu = Queue()
    #inputs=int(input())
    #while inputs>0:
    #command=input()
    #operation=command.split()
    if(op=="S"):
        print(Qu.size())
    elif(op=="I"):
        print(Qu.isEmpty())
    elif(op=="E"):
        Qu.enqueue(d)
        #Qu.printQueue()
    elif(op=="D"):
        print(Qu.dequeue()) #added print to print the popped out element
        #Qu.printQueue()
    elif(op=="F"):
        print(Qu.front())
    Qu.printQueue()

def main(a, b=0):
    testQueue(a, b)

if __name__ == '__main__':
    inputFile=open("queueInput.txt", "r")
    operations=inputFile.read().split(" ")
    print(operations)
    for i in range(0, len(operations), 1):
        if operations[i]=="E":
            main(operations[i], int(operations[i+1]))
            i+=1
        else:
            main(operations[i])
    