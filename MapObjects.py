class Client:
    def __init__(self, newStartx, newStarty, newBudget, newId):
        self.startx = newStartx
        self.starty = newStarty
        self.budget = newBudget
        self.id = newId

class Destination:
    def __init__(self, newEndx, newEndy, newId):
        self.endx = newEndx
        self.endy = newEndy
        self.id = newId

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"

arena = None

class Cell:
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy
 
        self.client = None
        self.destination = None
        self.directions = []
        self.taxi = None
 
    def getNeighbours(self, arena):
        neighbours = []
        
        if NORTH in self.directions:
            neighbours.append(arena[self.y - 1][self.x])
        if SOUTH in self.directions:
            neighbours.append(arena[self.y + 1][self.x])
        if EAST in self.directions:
            neighbours.append(arena[self.y][self.x + 1])
        if WEST in self.directions:
            neighbours.append(arena[self.y][self.x - 1])
        
        return neighbours
    
    def hasClient(self):
        return client != None
    
    def hasDestinationForClient(self, clientId):
        return destination != None and destination.id == clientId

class Taxi:
    def __init__(self, posx, posy, capacity):
        self.x = posx
        self.y = posy
        self.fuel = capacity

        self.money = 0
        self.client = None
