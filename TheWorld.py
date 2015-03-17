#Test 1
import random

class lsForBiomes():
    def selectBiome(self): # Assigns random biome for location
        the_number = random.randint(1,101)
        if the_number <= 3:
            biomeType = 1
        elif the_number <= 9:
            biomeType = 2
        elif the_number <= 17:
            biomeType = 3
        elif the_number <= 28:
            biomeType = 4
        elif the_number <= 42:
            biomeType = 5
        elif the_number <= 59:
            biomeType = 6
        elif the_number <= 78:
            biomeType = 7
        else:
            biomeType = 8
        return biomeType
    
    def selectDescrip(self, biomeType): # Assigns random description from a list according to its current biome
        
        urbanLs = ['Urban Descrip 1', 'Urban Descrip 2']
        aquaticLs = ['Aquatic Descrip 2', 'Aquatic Descrip 2']
        marshLs = ['Marsh Descrip 1', 'Marsh Descrip 2']
        desertLs = ['Desert Descrip 1', 'Desert Descrip 2']
        mountainLs = ['Mountain Descrip 1', 'Mountain Descrip 2']
        hillsLs = ['Hill Descrip 1', 'Hill Descrip 2']
        forestLs = ['Forst Descrip 1','Forest Descrip 2']
        plainsLs = ['Plains Descrip 1', 'Plains Descrip 2']
        dungeonLs = ['Dungeon Descrip 1', 'Dungeon Descrip 2']
        
        if biomeType == 1:
            biomeDescrip = random.choice(urbanLs)
        elif biomeType == 2:
            biomeDescrip = random.choice(aquaticLs)
        elif biomeType == 3:
            biomeDescrip = random.choice(marshLs)
        elif biomeType == 4:
            biomeDescrip = random.choice(desertLs)
        elif biomeType == 5:
            biomeDescrip = random.choice(mountainLs)
        elif biomeType == 6:
            biomeDescrip = random.choice(hillsLs)
        elif biomeType == 7:
            biomeDescrip = random.choice(forestLs)
        else:
            biomeDescrip = random.choice(plainsLs)
        return biomeDescrip

class Location(object):
    def __init__(self):
        self.BIOME = lsForBiomes.selectBiome(self) # Assign this instance of location's biome
        self.DESCRIP = lsForBiomes.selectDescrip(self, self.BIOME) # ^ but assigns description

    def __str__(self):
        the_string = "Hi! I am a location!\n"
        the_string += "\nI am the biomeType " + self.biomeDic[self.BIOME] + '.'
        the_string += "\nMy description is: " + self.DESCRIP + '.'
        return the_string
    
    biomeDic = { #Dictionary to retrieve string of the type of location
        0 : "Impassable",
        1 : "Urban",
        2 : "Aquatic",
        3 : "Marsh",
        4 : "Desert",
        5 : "Mountains",
        6 : "Hills",
        7 : "Forest",
        8 : "Plains",
        9 : "Dungeon",
        }

    
class World(object):
    def __init__(self, currentLocation):
        self.map = [Location() for i in range(36)] # initializes a list of locations, [Location 1, L2, L3, etc..]
        self.currentLocation = currentLocation
        #for i in range(len(self.map)):
            #print(self.map[i]) #PRINT ALL BIOMES
        
    def createDungeon(self): # Create the dungeon by replacing a random sqaure
        dungeonLs = ['Dungeon Descrip 1', 'Dungeon Descrip 2']
        dungeonIndex = random.randint(1,35)
        self.map[dungeonIndex].BIOME = 9
        self.map[dungeonIndex].DESCRIP = random.choice(dungeonLs)
        
    def createCity(self): # Same as dungeon
        CityLs = ['Urban Descrip 1', 'Urban Descrip 2']
        cityIndex = random.randint(1,35)
        self.map[CityIndex].BIOME = 1
        self.map[CityIndex].DESCRIP = random.choice(CityLs)

    def movePlayerN(self, currentLocation): # Move player (N)orth
        if (currentLocation - 6) < 0: # Check to move up
            return currentLocation
        else:
            currentLocation = currentLocation - 6 
            return currentLocation
        
    def movePlayerE(self, currentLocation):
        if (currentLocation + 1) % 6 == 0: # This is the check to see if you can move right.
            return currentLocation
        else:
            return currentLocation + 1
        
    def movePlayerS(self, currentLocation): 
        if (currentLocation + 6) > 35: # Check to move south
            return currentLocation
        else:
            currentLocation = currentLocation + 6
            return currentLocation
        
    def movePlayerW(self, currentLocation): # Check to move west
        if (currentLocation % 6) == 0:
            return currentLocation
        else:
            currentLocation = currentLocation - 1
            return currentLocation
    def printLocation(self, currentLocation):
        return currentLocation
        
    def getPositionBiome(self, currentLocation): # Retrieves biome of current location
        return self.map[currentLocation]

    
currentLocation = 0
world = World(currentLocation)
world.createDungeon()

moveWhere = input('Where would you like to move: ')
while moveWhere != 'q':
    if moveWhere == 'n':
        currentLocation = world.movePlayerN(currentLocation)
    elif moveWhere == 'e':
        currentLocation = world.movePlayerE(currentLocation)
    elif moveWhere == 's':
        currentLocation = world.movePlayerS(currentLocation)
    elif moveWhere == 'w':
        currentLocation = world.movePlayerW(currentLocation)
    elif moveWhere == 'l':
        print(str(world.printLocation(currentLocation)))
    elif moveWhere == 'b':
        print(world.getPositionBiome(currentLocation))
    elif moveWhere == 'q':
        print('Goodbye')
    else:
        print('Unknown Command')
    print(world.map[currentLocation])
    print('You are on sqaure', currentLocation)
    print()
    moveWhere = input('Where would you like to move: ')
