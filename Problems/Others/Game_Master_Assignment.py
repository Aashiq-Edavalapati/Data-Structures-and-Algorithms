"""
You are the designer of a randomized Treasure Hunt Simulator.
As part of your design, you have a game master who assigns dynamic quests to players.
Each player can complete the quest in any order.
The quest is generated at the beginning of the game and the first player to finish wins the game. 
Each player gets a random sequence of quests that may not be evenly distributed. 
The designer also does't know the number of players.
As the developer of this simultion create an appropriate solution involving an optimal data structure design and corresponding operations.
Calculate the time complexity of each of the operations and justify your choice and implementation with adequate explanation.
"""

import random

class PlayerLinkedList():
    class Node():
        def __init__(self, playerID):
            self.playerID = playerID
            self.quests = None
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, playerID):
        new_node = self.Node(playerID)
        if self.size == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1
    
    def print_player_quests(self):
        current_node = self.head
        while current_node != None:
            print(str(current_node.playerID) + " : " + str(current_node.quests))
            current_node = current_node.next

    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return "[]"
        players_str = "["
        current_node = self.head
        while current_node:
            players_str += str(current_node.playerID) + ", "
            current_node = current_node.next
        return players_str[:-2] + "]"


class PlayerQuestLinkedList():
    class Node():
        def __init__(self, quest):
            self.quest = quest
            self.status = False
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, quest):
        new_node = self.Node(quest)
        if self.size == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1

    def mark_complete(self, quest):
        current_node = self.head
        while current_node and current_node.quest != quest:
            current_node = current_node.next
        if current_node:
            current_node.status = True

    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return "[]"
        player_quests = "["
        current_node = self.head
        while current_node:
            player_quests += str(current_node.quest) + ": " + str(current_node.status) + ", "
            current_node = current_node.next
        return player_quests[:-2] + "]"


class AllQuestLinkedList():
    class Node():
        def __init__(self, quest):
            self.quest = quest
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, quest):
        new_node = self.Node(quest)
        if self.size == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1
    
    def get_quest(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of Bounds")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.quest     

    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return "[]"
        all_quests_str = "["
        current_node = self.head
        while current_node:
            all_quests_str += str(current_node.quest) + ", "
            current_node = current_node.next
        return all_quests_str[:-2] + "]"
    

class Game():
    def __init__(self):
        self.players = PlayerLinkedList()
        self.quests = AllQuestLinkedList()
        self.quests_init()
    
    def quests_init(self):
        self.quests.append("Find the red flower in the garden")
        self.quests.append("Look under the door mat")
        self.quests.append("Check inside the mailbox")
        self.quests.append("Search behind the big rock in the garden")
        self.quests.append("Look under the sink")
        self.quests.append("Find the blue book on the bookshelf")
        self.quests.append("Check inside the washing machine")
        self.quests.append("Look under the bed")
        self.quests.append("Search the golvebox in the car")
        self.quests.append("Look inside the refrigerator")
    
    def assign_quest(self, player):
        no_of_quests = random.randrange(1, 6)
        player_quests = PlayerQuestLinkedList()
        for _ in range(no_of_quests):
            quest_index = random.randrange(0, len(self.quests))
            player_quests.append(self.quests.get_quest(quest_index))
        player.quests = player_quests
    
    def find_winner(self):
        if self.players.head is None:
            return None
        fastest = self.players.head
        current_node = self.players.head
        while current_node != None:
            if len(current_node.quests) < len(fastest.quests):
                fastest = current_node
            current_node = current_node.next
        return fastest.playerID
    

def main():
    treasure_hunt = Game()
    player_num = int(input("Enter the number of players: "))
    for _ in range(player_num):
        player_id = input("Enter Player ID: ")
        treasure_hunt.players.append(player_id)
        player_node = treasure_hunt.players.head
        while player_node.next != None:
            player_node = player_node.next
        treasure_hunt.assign_quest(player_node)
    treasure_hunt.players.print_player_quests()
    print("The winner is:", treasure_hunt.find_winner())


if __name__ == "__main__":
    main()
