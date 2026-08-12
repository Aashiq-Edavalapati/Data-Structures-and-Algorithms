'''
    Your team is designing a text editor and is responsible for implementing the undo and 
redo functionality. The goal is to create a data structure that records actions 
performed by the user, allowing for actions to be undone and redone. When a user 
makes a change, such as inserting or deleting text, the action is recorded. Implement 
methods to add actions, undo the last action, and redo the last undone action. Define 
actions with details including type (e.g., insert, delete) and relevant data (e.g., text 
and position). Develop functions for perform_action(action), undo(), and 
redo(), and implement a command-line interface for user interaction where users 
can type text to perform insert operations, type "undo" to revert the last action, and 
type "redo" to reapply the last undone action. The program should display the current 
state of the text after each operation and provide appropriate messages if undo or 
redo operations are not possible. The perform_action function records the action, 
clears the redo history, applies the change to the text, and updates the display. The 
undo function reverts the last action if possible, transferring it to the redo stack, and 
the redo function re-applies the last undone action from the redo stack.  
Test Case: 
a. perform_action({"type": "insert", "text": "Hello", "position": 0})  
Current text: Hello  
b. perform_action({"type": "insert", "text": " World", "position": 5})  
Current text: Hello World  
c. undo()  
Undo last action.  
Current text: Hello  
d. redo()  
Redo last action.  
Current text: Hello World 
'''

class TextEditor:
    class Node:
        def __init__(self,text) -> None:
            self.text = text
            self.next = None

    def __init__(self) -> None:
        self.head = None
        self.actions = 0
        self.lastAction = None

    def perform_action(self,action):
        newAction = self.Node(action)
        newAction.next = self.head
        self.head = newAction
        


    def undo(self):
        pass

    def redo(self):
        pass

    def insert(self,text,position):
        pass

class ActionStack:
    pass