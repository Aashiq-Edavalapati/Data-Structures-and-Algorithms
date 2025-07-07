'''
    You are a designer of a randomized treasurehunt simulator. As part of your design you have a game master 
    who assigns quests to players. Each player can complete the quest in any order. The quests are generated
    at the beginning of the game and the player that finishes all the quests first wins the game. Each player
    has a random sequence of quests and may not be the same number evenly distributed. The designer also does
    not know the number of players.As the developer, of this simulation create an appropriate solution involving 
    optimal data structure design with appropriate solution and corresponding operations. 
    
    Calculate time complexity of each of the operations and justify your choice and implementation appropriately.
'''

import random

class QuestNode:
    def __init__(self, quest):
        self.quest = quest
        self.next = None

class PlayerNode:
    def __init__(self, player_id):
        self.player_id = player_id
        self.quests_head = None
        self.next = None

class PlayerLinkedList:
    def __init__(self):
        self.head = None

    def add_player(self, player_id):
        new_player = PlayerNode(player_id)
        if not self.head:
            self.head = new_player
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_player
    

class QuestLinkedList:
    def __init__(self):
        self.head = None

    def add_quest(self, quest):
        new_quest = QuestNode(quest)
        if not self.head:
            self.head = new_quest
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = new_quest

    def containsQuest(self,quest):
        currentNode = self.head
        while currentNode:
            if currentNode.quest == quest:
                return True
            currentNode = currentNode.next
        return False


class TreasureHunt:
    def __init__(self) -> None:
        self.quests = QuestLinkedList()
        self.players = PlayerLinkedList()

    def generateQuests(self):
        print("Welcome Game Master, Please assign some quests for the treasure hunt!!")
        enterMoreQuests = True
        while enterMoreQuests:
            quest = input("Enter the quest description: ")
            self.quests.add_quest(quest)
            enterMoreQuests = input("Do you want to enter more quests? (Y/N)").lower() == 'y'
    
    def enrollPlayers(self):    
        enrollMorePlayers = True
        while enrollMorePlayers:
            playerId = input("Enter the id of the enrolling player: ")
            self.players.add_player(playerId)
            enrollMorePlayers = input("Do you want to enroll more players? (Y/N)").lower() == 'y'
    
    def assignQuest(self,player):
        size = 1
        personalQuests = QuestLinkedList()
        currentNode = self.quests.head
        while currentNode.next:
            size += 1
            currentNode = currentNode.next
        noOfQuests = random.randint(1,size)
        while noOfQuests > 0:
            questPosition = random.randint(1,size)
            currentPosition = 1
            currentNode = self.quests.head
            while currentPosition < questPosition:
                currentNode = currentNode.next
                currentPosition += 1
            if not self.quests.containsQuest(currentNode.quest):
                temp = QuestNode(currentNode.quest)
                personalQuests.add_quest(temp)
                noOfQuests -= 1
        player.quest_head = personalQuests.head

    def assignQuests(self):
        currentNode = self.players.head
        while currentNode:
            self.assignQuest(currentNode)
            currentNode = currentNode.next

