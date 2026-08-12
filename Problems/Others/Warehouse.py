
'''
    Preamble:
        This class represents a warehouse, which contains several containers.

        Class Signature:
            Warehouse(self: Self@Warehouse) -> None

        Parameters:
            -> head: Contains head of the first container in the warehouse. :Container
            -> containers: Contains count of the containers that are currently available in the warehouse.

        Methods:
            1) def noOfContainers(self: Self@Warehouse) -> int
                To return count of the containers in warehouse.
            
            2) def addItem(self: Self@Warehouse, item: Any) -> None
                Adds a new item to the warehouse. Adds item into a container which has items of the same type.
                If there is no such container present then new container will be created.

            3) def removeItem(self: Self@Warehouse, type: Any) -> None
                Removes a specified item from the container and the warehouse.
            
            4) def getCountOfItems(self: Self@Warehouse, type: Any) -> (int | None)
                Returns the total number of item of a specified type in the warehouse.

            5) def arrangeContainers(self: Self@Warehouse) -> None
                Arranges the containers in the increasing order of the count of items in the container.

            6) def swap(self: Self@Warehouse, container1: Any, container2: Any) -> None
                Helper function to swap two nodes when arranging the containers.
'''
class Warehouse:
    class Containers:
        def __init__(self,container) -> None:
            self.container = container
            self.next = None
    def __init__(self) -> None:
        self.head = None
        self.containers = 0

    def noOfContainers(self):
        return self.containers

    def addItem(self, item):
        if self.head is None:
            self.head = self.Containers(Container())
            self.containers += 1
            self.head.container.addItem(item)
        else:
            currentContainer = self.head
            added = False
            while currentContainer.next != None:
                if currentContainer.container.top() is None:
                    currentContainer.container.addItem(item)
                    added = True
                    break
                if currentContainer.container.top() == item:
                    currentContainer.container.addItem(item)
                    added = True
                    break
                currentContainer = currentContainer.next
            if not added and currentContainer.container.top() == item:
                currentContainer.container.addItem(item)
                added = True
            if not added:
                currentContainer.next = self.Containers(Container())
                self.containers += 1
                currentContainer.next.container.addItem(item)
        
                
    def removeItem(self,type):
        if self.head is None:
            print("There are no containers!!")
            return
        if self.head.next is None:
            self.head.container.removeItem()
            return
        currentContainer = self.head
        removed = False
        while currentContainer.next != None:
            if currentContainer.container.top() == type:
                currentContainer.container.removeItem()
                removed = True
            currentContainer = currentContainer.next
        if not removed and currentContainer.container.top() == type:
            currentContainer.container.removeItem()
            return
        if not removed:
            print("There is no container with given type of items!!")
        
    def getCountOfItems(self,type):
        if self.head is None:
            print("There are no containers!!")
        else:
            currentContainer = self.head
            while currentContainer:
                if currentContainer.container.top() == type:
                    return currentContainer.container.noOfItems()
                currentContainer = currentContainer.next
            print("There is no container given type of item!!")
            return None
        
    def printContainersAndItems(self):
        if self.head is None:
            print("There are no containers!!")
            return
        currentContainer = self.head
        while currentContainer:
            currentContainer.container.printContainer()
            currentContainer = currentContainer.next
    
    def arrangeContainers(self):
        if self.head is None:
            print("There are no containers!!")
            return
        
        swapped = True
        while swapped:
            swapped = False
            currentContainer = self.head
            while currentContainer.next:
                if currentContainer.container.items < currentContainer.next.container.items:
                    self.swap(currentContainer,currentContainer.next)
                    swapped = True
                currentContainer = currentContainer.next
    
    def swap(self,container1,container2):
        temp = container2.container
        container2.container = container1.container
        container1.container = temp

    def printContainers(self):
        if self.head is None:
            print("There are not containers!!")
            return
        currentContainer = self.head
        while currentContainer:
            print(currentContainer.container.top(),end='->')
            currentContainer = currentContainer.next
        print("End")


'''
    Preamble:
        This class represents a container in warehouse. Each container stores only one type of item.

        Class Signature:
            Container(self: Self@Container) -> None
        
        Parameters:
            1) head: Contains the top most item of the container.

            2) items: Contains the count of items in that particular container.

        Methods:
            1) def top(self: Self@Container) -> (Any | None)
                Returns the content of the top most item in the container if there is an item in the container.
            
            2) def noOfItems(self: Self@Container) -> int
                Returns the count of items in the container.
            
            3) def addItem(self: Self@Container, item: Any) -> None
                Adds a new item to the container.
            
            4) def removeItem(self: Self@Container) -> None
                Removes and returns the top most item of the container if there is an item in the container.
'''

class Container:
    class Item:
        def __init__(self,item) -> None:
            self.item = item
            self.next = None

    def __init__(self) -> None:
        self.head = None
        self.items = 0

    def top(self):
        if self.head is None:
            print("Empty Container")
        else:
            return self.head.item

    def noOfItems(self):
        return self.items
    
    def addItem(self,item):
        newItem = self.Item(item)
        newItem.next = self.head
        self.head = newItem
        self.items += 1

    def removeItem(self):
        if self.head is None:
            print("Container is empty!!")
            return
        temp = self.head
        self.head = self.head.next
        del temp
        self.items -= 1

    def printContainer(self):
        if self.head is None:
            print("Container is empty!!")
            return
        currentItem = self.head
        while currentItem:
            print(currentItem.item, end="->")
            currentItem = currentItem.next
        print("End")

def process_file(input_file, output_file):
    warehouse = Warehouse()

    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        for line in infile:
            operation = line.strip()
            
            if operation.startswith("ADD"):
                item = operation[4:]  # Extract the item after "ADD "
                warehouse.addItem(item)
                # outfile.write(f"Added {item}\n")
                
            elif operation.startswith("REMOVE"):
                item = operation[7:]  # Extract the item after "REMOVE "
                warehouse.removeItem(item)
                # outfile.write(f"Removed {item}\n")
                
            elif operation.startswith("COUNT"):
                item = operation[6:]  # Extract the item after "COUNT "
                count = warehouse.getCountOfItems(item)
                if count is not None:
                    outfile.write(f"Count of {item}: {count}\n")
                    
            elif operation == "PRINT":
                outfile.write("Printing all containers:\n")
                current_container = warehouse.head
                while current_container:
                    current_item = current_container.container.head
                    while current_item:
                        outfile.write(f"{current_item.item}->")
                        current_item = current_item.next
                    outfile.write("End\n")
                    current_container = current_container.next
                
            elif operation == "ARRANGE":
                warehouse.arrangeContainers()
                outfile.write("Containers arranged\n")

if __name__ == '__main__':
    outputFile = open('Problems\Warehouse Output.txt','w')
    outputFile.write('Test Case 1:\n')
    outputFile.close()
    process_file("Problems\Warehouse Input.txt","Problems\Warehouse Output.txt")
    outputFile = open('Problems\Warehouse Output.txt','a')
    outputFile.write('\nTest Case 2:\n')
    outputFile.close()
    process_file("Problems\Warehouse TestCase2.txt","Problems\Warehouse Output.txt")
    outputFile = open('Problems\Warehouse Output.txt','a')
    outputFile.write('\nTest Case 3:\n')
    outputFile.close()
    process_file("Problems\Warehouse TestCase3.txt","Problems\Warehouse Output.txt")