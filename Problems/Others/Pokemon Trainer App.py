class Pokemon:
    class Node:
        def __init__(self,name,specie,level,nature) -> None:
            self.pokemon = name
            self.specie = specie
            self.level = level
            self.nature = nature
            self.fav = None
            self.activities = Activity()
            self.next = None
            self.undoStack = Stack()
            self.redoStack = Stack()

        def undo(self):
            if self.undoStack.isEmpty():
                print(f"Cannot undo. No previous activity available for {self.pokemon}.")
                return
            undoneAction = self.undoStack.pop()
            self.redoStack.push(undoneAction)
            self.activities.decreaseActivityCount(undoneAction)
            print(f'Undo last activity for {self.pokemon}: {undoneAction}.')

        def redo(self):
            if self.redoStack.isEmpty():
                print(f"Cannot redo. No undone activity available for {self.pokemon}.")
                return
            redoneAction = self.redoStack.pop()
            self.undoStack.push(redoneAction)
            self.activities.increaseActivityCount(redoneAction)
            print(f'Redo last activity for {self.pokemon}: {redoneAction}.')

    def __init__(self) -> None:
        self.firstPokemon = None
        self.pokemonCount = 0
        
    
    def addPokemon(self,pokemon,specie,level,nature):
        if self.firstPokemon is None:
            self.firstPokemon = self.Node(pokemon,specie,level,nature)
        else:
            currentPokemon = self.firstPokemon
            while currentPokemon.next:
                currentPokemon = currentPokemon.next
            currentPokemon.next = self.Node(pokemon,specie,level,nature)
        self.pokemonCount += 1

    def getFavoriteActivity(self,pokemon):
        if self.firstPokemon is None:
            print("There are no pokemons in your  inventory currently!!")
            return

        currentPokemon = self.firstPokemon
        while currentPokemon:
            if currentPokemon.pokemon == pokemon:
                print(f"Favorite activity of {pokemon} : {currentPokemon.activities.findFavoriteActivity()}")
                return
            currentPokemon = currentPokemon.next

        if not currentPokemon:
            print("The pokemon you specified is not in the inventory!!")

    def performAction(self,pokemon,activity):
        if self.firstPokemon is None:
            print("There are no pokemons in your  inventory currently!!")
            return

        currentPokemon = self.firstPokemon
        while currentPokemon:
            if currentPokemon.pokemon == pokemon:
                currentPokemon.activities.doActivity(activity)
                print(f"Performed {activity} activity for {pokemon}")
                currentPokemon.undoStack.push(activity)
                return
            currentPokemon = currentPokemon.next

        if not currentPokemon:
            print("The pokemon you specified is not in the inventory!!")
    
    def undo(self,pokemon):
        if self.firstPokemon is None:
            print("There are no pokemons!!!")
            return
        currentPokemon = self.firstPokemon
        while currentPokemon:
            if currentPokemon.pokemon == pokemon:
                currentPokemon.undo()
                return
            currentPokemon = currentPokemon.next
        print("There is no such pokemon!!")
    
    def redo(self,pokemon):
        if self.firstPokemon is None:
            print("There are no pokemons!!")
            return
        currentPokemon = self.firstPokemon
        while currentPokemon:
            if currentPokemon.pokemon==pokemon:
                currentPokemon.redo()
                return
            currentPokemon = currentPokemon.next
        print("There is no such pokemon!!!")


class Activity:
    class Node:
        def __init__(self,activity) -> None:
            self.activity = activity
            self.freq = 0
            self.next = None
    def __init__(self) -> None:
        self.firstActivity = None
    
    def addActivity(self,activity):
        if self.firstActivity is None:
            self.firstActivity = self.Node(activity)
        else:
            currentActivity = self.firstActivity
            while currentActivity.next:
                currentActivity = currentActivity.next
            currentActivity.next = self.Node(activity)
    
    def doActivity(self,activity):
        currentActivity = self.firstActivity
        while currentActivity:
            if currentActivity.activity == activity:
                currentActivity.freq += 1
                return
            currentActivity = currentActivity.next
        self.addActivity(activity)
    
    def findFavoriteActivity(self):
        if self.firstActivity is None:
            print("Sorry there are no activities that this pokemon does!!")
            return
        maxFreq = -1
        favActivity = None
        currentActivity = self.firstActivity
        while currentActivity.next:
            if currentActivity.freq > maxFreq:
                maxFreq = currentActivity.freq
                favActivity = currentActivity.activity
            currentActivity =currentActivity.next
        return favActivity
            

    def decreaseActivityCount(self,activity):
        if self.firstActivity is None:
            print("Sorry there are no activities!!!")
            return
        currentActivity = self.firstActivity
        while currentActivity:
            if currentActivity.activity == activity:
                currentActivity.freq -= 1
                return
            currentActivity = currentActivity.next
        print("There is no such action!!")
    
    def increaseActivityCount(self,activity):
        if self.firstActivity is None:
            print("Sorry there are no activities!!!")
            return
        currentActivity = self.firstActivity
        while currentActivity:
            if currentActivity.activity == activity:
                currentActivity.freq += 1
                return
            currentActivity = currentActivity.next
        print("There is no such action!!")



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
    pokemonInventory = Pokemon()

    while True:
        operation = input().strip()

        if operation == "End":
            break
        
        li = operation.split()

        if len(li) == 2:
            action, pokemonName = li[0], li[1]

            if action == "F":
                pokemonInventory.performAction(pokemonName, "Feeding")
            elif action == "T":
                pokemonInventory.performAction(pokemonName, "Training")
            elif action == "B":
                pokemonInventory.performAction(pokemonName, "Battling")
            elif action == "U":
                pokemonInventory.undo(pokemonName)
            elif action == "R":
                pokemonInventory.redo(pokemonName)
            elif action == "Fav":
                pokemonInventory.getFavoriteActivity(pokemonName)

        elif len(li) == 4 and li[0] == "Add":
            pokemonName, specie, levelAndNature = li[1:]
            level, nature = levelAndNature.split(',')
            pokemonInventory.addPokemon(pokemonName, specie, int(level), nature)
        else:
            print("Invalid operation!")

