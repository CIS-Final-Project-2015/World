#Dungeon test 1

import random


class dunWorld(object):
    def __init__(self):
        dungeonLs = ['dungeon1.txt', 'dungeon2.txt']
        dungeonTxt = random.choice(dungeonLs)
        self.dungeonFile = open(dungeonTxt, "r")
        self.dungeon = [dungeonLocation() for i in range(36)]
        for i in range(len(self.dungeon)):
            form = self.dungeonFile.readline()
            form = form.strip()
            form = form.split(',')
            self.dungeon[i].dungeonForm = form
            if self.dungeon[i].dungeonForm.count('1') == 1: #Tells if a square is a room or not
                self.dungeon[i].room = True
            try:
                if self.dungeon[i].dungeonForm[4]: #Check if square is final square
                    self.dungeon[i].final = True
            except IndexError:
                pass
        
        self.spawnLocation = self.dungeonFile.readline() # Reads last line for spawn point location
        self.spawnLocation = self.spawnLocation.strip()
        self.spawnLocation = int(self.spawnLocation)
        
        self.dungeonFile.close()
        self.__makeDoors() #Chooses which rooms will have doors 


##############################################################
        
    def possibleMoves(self, currentLocation):
        string = "You can move:\n"
        if self.dungeon[currentLocation].dungeonForm[0] == '1':
            string += "\t- North \n"
        if self.dungeon[currentLocation].dungeonForm[1] == '1':
            string += "\t- East \n"
        if self.dungeon[currentLocation].dungeonForm[2] == '1':
            string += "\t- South \n"
        if self.dungeon[currentLocation].dungeonForm[3] == '1':
            string += "\t- West \n"
        return string    
                
    def MovePlayerN(self, currentLocation): # Move player (N)orth
        if self.dungeon[currentLocation].dungeonForm[0] == '1':# Check to move up
            return currentLocation - 6
        else:
            return currentLocation
        
    def MovePlayerE(self, currentLocation):
        if self.dungeon[currentLocation].dungeonForm[1] == '1': # This is the check to see if you can move right.
            return currentLocation + 1
        else:
            return currentLocation
        
    def MovePlayerS(self, currentLocation): 
        if self.dungeon[currentLocation].dungeonForm[2] == '1': # Check to move south
            return currentLocation + 6
        else:
            return currentLocation
        
    def MovePlayerW(self, currentLocation): # Check to move west
        if self.dungeon[currentLocation].dungeonForm[3] == '1':
            return currentLocation - 1
        else:
            return currentLocation
        
##########################################################

    def getRooms(self): # This will return a list of what squares are rooms
        rooms = []
        for i in range(len(self.dungeon)):
            if self.dungeon[i].room == True:
                rooms.append(i)
        return rooms 

    def __makeDoors(self):
        rooms = self.getRooms()
        numDoors = random.randrange(len(rooms))
        templist = rooms
        for i in range(numDoors):
            choice = random.choice(templist)
            self.dungeon[choice].door = True
            templist.remove(choice)

    def returnDoor(self, currentLocation):
        roomAtrib = []
        if self.dungeon[currentLocation].room == True:
            if self.dungeon[currentLocation].door == True:
                roomAtrib.append(1)
            else:
                roomArtib.append(0)
            if self.dungeon[currentLocation].locked == True:
                roomAtrib.append(1)
            else:
                roomAtrib.append(0)
        else:
            print("\nERROR CURRENT LOCATION NOT A ROOM\n")
            
        return roomAtrib
    def unlockDoor(self, currentLocation): #To unlock a door at your current position
        if self.dungeon[currentLocation].door == True:
            if self.dungeon[currentLocation].locked == True:
                self.dungeon[currentLocation].locked = False
        else:
            print('\nERROR NO DOOR PRESENT OR DOOR IS ALREADY UNLOCKED\n')
        
                        
    
class dungeonLocation(object):
    dungeonForm = []        #[N,E,S,W] a list of exits.
    room = None             #Defines if a square is a room
    door = False            #If there is a door in this location
    locked = True           #This will have to be toggled when a door is locked/unlocked
    final = False           #If this square is the final square

    def __str__(self):
        string = "Dungeon Form: "
        string += ','.join(self.dungeonForm)
        string += '\n'
        
        string += "Room: "
        if self.room == None:
            string += "None"
        else: 
            string += "True"
        
        string += "\nDoor: "
        if self.door == True:
            string += "True\n"
            string += "Locked: "
            if self.locked == True:
                string += "True\n"
            else:
                string += "False\n"
        else:
            string += "False\n"
            
        string += "Final Square: "
        if self.final == True:
            string += "True\n"
        else:
            string += "False\n"
        return string
#Main
def launchDungeon():
    print('You are in an eerie dungeon...')
 
    dungeonWorld = dunWorld()
    currentLocation = dungeonWorld.spawnLocation #This will change your location to the spawn point on the map
    
    ################# Simple UI ##################
    inDungeon = True
    moveWhere = None
    while inDungeon == True:
        
        if moveWhere == 'n':
            currentLocation = dungeonWorld.MovePlayerN(currentLocation)
        elif moveWhere == 'e':
            currentLocation = dungeonWorld.MovePlayerE(currentLocation)
        elif moveWhere == 's':
            currentLocation = dungeonWorld.MovePlayerS(currentLocation)
        elif moveWhere == 'w':
            currentLocation = dungeonWorld.MovePlayerW(currentLocation)
        elif moveWhere == 'return':
            doorCheck = dungeonWorld.returnDoor(currentLocation)
            if doorCheck:
                if doorCheck[0] == 1:
                    print('\nTheres a door here.')
                    if doorCheck[1] == 1:
                        print('It is locked also.\n')
            else:
                print('There is no door here')
        elif moveWhere == 'u':
            dungeonWorld.unlockDoor(currentLocation)
        #elif moveWhere == 'q': Un-comment this to add a quit function that'll take you out of the dungeon
            #print('Goodbye')   and straight back where you were in the world
            #inDungeon = False
            #break
            
        elif moveWhere == None:
            pass
        else:
            print('Unknown Command')
    
        if dungeonWorld.dungeon[currentLocation].final == True:
            print('You are in the exit square!')
            decide = input('Would you like to leave the dungeon:')
            if decide == 'y':
                currentLocation = random.randrange(35)
                inDungeon = False
                return currentLocation
        
        print(dungeonWorld.possibleMoves(currentLocation))
        
        #print(dungeonWorld.dungeon[currentLocation]) #Uncomment this to enable debug
        
        moveWhere = input('Where would you like to move: ')


