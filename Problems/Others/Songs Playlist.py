class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack empty raa pookaa!!!")
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp.data

    def getSize(self):
        return self.size

class PlaylistNode:
    def __init__(self,song):
        self.song = song
        self.next = None
        self.previous = None

class Playlist:
    def __init__(self):
        self.firstSong = None
        self.songsCount = 0
        self.currentSong = None
        self.redoStack = Stack()
        self.undoStack = Stack()
    
    def addSong(self,song):
        if self.songsCount == 0:
            self.firstSong = PlaylistNode(song)
            self.currentSong = self.firstSong
        else:
            currentSong = self.firstSong
            while currentSong.next:
                currentSong = currentSong.next
            currentSong.next = PlaylistNode(song)
            currentSong.next.previous = currentSong
        self.songsCount += 1
        self.undoStack.push(f"addSong {song}")
    
    def playNextSong(self):
        if self.currentSong.next == None:
            return "Paatalaipoyyay!!"
        else:
            self.currentSong = self.currentSong.next
            self.undoStack.push("Next")
            return f"Playing {self.currentSong.song}"
        
    
    def playPreviousSong(self):
        if self.currentSong.previous == None:
            return "Ide first song!!"
        else:
            self.currentSong = self.currentSong.previous
            self.undoStack.push("Prev")
            return f'Playing {self.currentSong.song}'
        
    
    def undo(self):
        if self.undoStack.head == None:
            return "No actions to undo!!"
        else:
            action = self.undoStack.pop()
            self.redoStack.push(action)
            if action.startswith("addSong"):
                currentSong = self.firstSong
                if currentSong.next is None:
                    self.firstSong = None
                    self.currentSong = None
                else:
                    while currentSong.next and currentSong.next.next:
                        currentSong = currentSong.next
                    currentSong.next = None
                self.songsCount -= 1
            elif action.startswith("Next"):
                self.playPreviousSong()
            elif action.startswith("Prev"):
                self.playNextSong()
                
    def redo(self):
        if self.redoStack.head == None:
            return "No actions to redo!!"
        else:
            action = self.redoStack.pop()
            self.undoStack.push(action)
            if action.startswith("addSong"):
                self.addSong(action[8:])
            elif action.startswith("Next"):
                self.playNextSong()
            elif action.startswith("Prev"):
                self.playPreviousSong()
        
if __name__ == "__main__":
    i = 1
    with open("Problems\Songs Playlist Input.txt",'r') as inputFile, open("Problems\Songs Playlist Output.txt",'w') as outputFile:
        testcase_flag = False
        playlist = None

        while True:
            line = inputFile.readline()
            if not line:
                break

            line = line.strip()
            if line.startswith("TESTCASE"):
                if testcase_flag:
                    outputFile.write("\n")
                testcase_flag = True
                outputFile.write(f"{line}\n")
                playlist = Playlist()

            elif line.startswith("ADD"):
                song_name_start = line.find("song")
                song = line[song_name_start:]
                playlist.addSong(song)
                outputFile.write(f"Added {song}\n")

            elif line == "NEXT":
                result = playlist.playNextSong()
                if result:
                    outputFile.write(result + "\n")

            elif line == "PREV":
                result = playlist.playPreviousSong()
                if result:
                    outputFile.write(result + "\n")

            elif line == "UNDO":
                result = playlist.undo()
                if result:
                    outputFile.write(result + "\n")

            elif line == "REDO":
                result = playlist.redo()
                if result:
                    outputFile.write(result + "\n")