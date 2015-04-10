#Test 1
import random
import DungeonWorld

class lsForBiomes():
    urbanLs = ['Urban Descrip 1', 'Urban Descrip 2']
    aquaticLs = ['Aquatic Descrip 2', 'Aquatic Descrip 2']
    marshLs = ['Marsh Descrip 1', 'Marsh Descrip 2']
    desertLs = ['Desert Descrip 1', 'Desert Descrip 2']
    mountainLs = ['Mountain Descrip 1', 'Mountain Descrip 2']
    hillLs = ['Hill Descrip 1', 'Hill Descrip 2']
    forestLs = ['Forst Descrip 1','Forest Descrip 2']
    plainLs = ['Plains Descrip 1', 'Plains Descrip 2']
    dungeonLs = ['Dungeon Descrip 1', 'Dungeon Descrip 2']
    
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
        if biomeType == 1:
            biomeDescrip = random.choice(lsForBiomes.urbanLs)
        elif biomeType == 2:
            biomeDescrip = random.choice(lsForBiomes.aquaticLs)
        elif biomeType == 3:
            biomeDescrip = random.choice(lsForBiomes.marshLs)
        elif biomeType == 4:
            biomeDescrip = random.choice(lsForBiomes.desertLs)
        elif biomeType == 5:
            biomeDescrip = random.choice(lsForBiomes.mountainLs)
        elif biomeType == 6:
            biomeDescrip = random.choice(lsForBiomes.hillLs)
        elif biomeType == 7:
            biomeDescrip = random.choice(lsForBiomes.forestLs)
        else:
            biomeDescrip = random.choice(lsForBiomes.plainLs)
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
    
    def __init__(self):
        self.map = [Location() for i in range(36)] # initializes a list of locations, [Location 1, L2, L3, etc..]
        #self.currentLocation = currentLocation
        
        self.__createDungeon()
        self.__createCity() # Create a city if none was already made.
        
        while self.map[0].BIOME == 2: #So you can't spawn on water
            self.BIOME = lsForBiomes.selectBiome(self) # Assign this instance of location's biome
            self.DESCRIP = lsForBiomes.selectDescrip(self, self.BIOME)

        #for i in range(len(self.map)):
            #print(self.map[i]) #PRINT ALL BIOMES

    def __createDungeon(self): # Create the dungeon by replacing a random sqaure
        dungeonLs = lsForBiomes.dungeonLs
        for i in range(random.randint(1,3)):
            dungeonIndex = random.randint(1,35)
            while self.map[dungeonIndex].BIOME == 1: # So it doesn't replace a city
                dungeonIndex = random.randint(1,35)
            self.map[dungeonIndex].BIOME = 9
            self.map[dungeonIndex].DESCRIP = random.choice(dungeonLs)
        
    def __createCity(self): # Same as Create dungeon
        count = 0
        for i in range(len(self.map)): # Check if any cities were generated
            if self.map[i].BIOME == 1:
                count += 1
        CityLs = lsForBiomes.urbanLs
        cityIndex = random.randint(1,35)
        if count <= 1:
            while self.map[cityIndex].BIOME == 9: # So it doesn't replace a dungeon
                cityIndex = random.randint(1,35)
            self.map[cityIndex].BIOME = 1
            self.map[cityIndex].DESCRIP = random.choice(CityLs)

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
        
    def getSurroundings(self, currentLocation):
        string = "******* Your surroundings *****"
        string += "\nYou are in a " + self.map[currentLocation].biomeDic[self.map[currentLocation].BIOME] + " biome."
        string += "\n\nYou can see: "
        if (currentLocation - 6) > 0: #N
            string += "\n\nNorth:\n\t"
            string += self.map[currentLocation - 6].DESCRIP
        if (currentLocation + 1) % 6 > 0: #E
            string += "\n\nEast:\n\t"
            string += self.map[currentLocation + 1].DESCRIP
        if (currentLocation + 6) < 35: #S
            string += "\n\nSouth:\n\t"
            string += self.map[currentLocation + 6].DESCRIP
        if (currentLocation % 6) > 0: #W
            string += "\n\nWest:\n\t"
            string += self.map[currentLocation - 1] .DESCRIP
        string += "\n********************************\n"
        return string
    
    def returnBiome(self, currentLocation): # Returns an integer of the biome type the player is CURRENTLY in.
        return self.map[currentLocation.BIOME]

#Main
currentLocation = 0 # you will need this for the world to function
world = World()# If your making your own main you will need to remove this




############# Simple UI ##############
print(world.getSurroundings(currentLocation))
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
        print(world.returnBiome(currentLocation))
    elif moveWhere == 'q':
        print('Goodbye')
        break
    else:
        print('Unknown Command\n')
    if world.map[currentLocation].BIOME == 9:
        decide = input('A dungeon appears before you! Would you like to enter it:')
        if decide == 'y':
            currentLocation = DungeonWorld.launchDungeon()
    print(world.getSurroundings(currentLocation))
    print()
    moveWhere = input('Where would you like to move: ')
