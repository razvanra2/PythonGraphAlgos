from MapObjects import *
from iohandler import *
import heapq

class SearchAlgorithms:
    @staticmethod
    def BFS(startCell, arena, taxi, destinationSearch):
        closedList = []
        for _ in range(len(arena)):
            closedList.append([False] * len(arena[0]))

        openList = [startCell]
        pi = { startCell: None }
        end = None

        while openList:
            s = openList.pop(0)

            if (not destinationSearch and s.client is not None):
                taxi.client = s.client
                taxi.x = s.x
                taxi.y = s.y
                
                s.client = None
                s.taxi = taxi

                startCell.taxi = None

                end = s
                break

            elif (destinationSearch and s.destination is not None
            and taxi.client.id == s.destination.id):
                taxi.money += taxi.client.budget
                taxi.client = None
                taxi.x = s.x
                taxi.y = s.y

                end = s
                s.taxi = taxi
                s.destination = None
                
                startCell.taxi = None

                break

            neighbouringCells = s.getNeighbours(arena)
            for cell in neighbouringCells:
                if (closedList[cell.y][cell.x] == False):
                    openList.append(cell)
                    pi[cell] = s

            closedList[s.y][s.x] = True

        temp = end
        path = []
        while (temp is not None):
            path.append(f'[{temp.y},{temp.x}]')
            temp = pi[temp]

        path.reverse()
        return path

    @staticmethod
    def UCS(startCell, arena, taxi, destinationSearch):
        closedList = []
        for _ in range(len(arena)):
            closedList.append([False] * len(arena[0]))

        openList = []
        heapq.heappush(openList, (0, startCell))
        pi = {startCell: None}
        end = None
        costDict = {startCell: 0}

        while openList:
            _,s = heapq.heappop(openList)

            if (not destinationSearch and s.client is not None):
                taxi.client = s.client
                taxi.x = s.x
                taxi.y = s.y

                s.client = None
                s.taxi = taxi

                startCell.taxi = None

                end = s
                break

            elif (destinationSearch and s.destination is not None
                  and taxi.client.id == s.destination.id):
                taxi.money += taxi.client.budget
                taxi.client = None
                taxi.x = s.x
                taxi.y = s.y

                end = s
                s.taxi = taxi
                s.destination = None

                startCell.taxi = None

                break

            neighbouringCells = s.getNeighbours(arena)
            for cell in neighbouringCells:
                if (closedList[cell.y][cell.x] == False):
                    pi[cell] = s
                    costDict[cell] = costDict[s] + 1
                    heapq.heappush(openList, (costDict[cell], cell))

            closedList[s.y][s.x] = True

        temp = end
        path = []
        while (temp is not None):
            path.append(f'[{temp.y},{temp.x}]')
            temp = pi[temp]

        path.reverse()
        return path

    @staticmethod
    def DFS(startCell, arena, taxi, destinationSearch):
        closedList = []
        for _ in range(len(arena)):
            closedList.append([False] * len(arena[0]))

        openList = [startCell]
        pi = {startCell: None}
        end = None

        while openList:
            s = openList.pop()

            if (not destinationSearch and s.client is not None):
                taxi.client = s.client
                taxi.x = s.x
                taxi.y = s.y

                s.client = None
                s.taxi = taxi

                startCell.taxi = None

                end = s
                break

            elif (destinationSearch and s.destination is not None
                  and taxi.client.id == s.destination.id):
                taxi.money += taxi.client.budget
                taxi.client = None
                taxi.x = s.x
                taxi.y = s.y

                end = s
                s.taxi = taxi
                s.destination = None

                startCell.taxi = None

                break

            neighbouringCells = s.getNeighbours(arena)
            for cell in neighbouringCells:
                if (closedList[cell.y][cell.x] == False):
                    openList.append(cell)
                    pi[cell] = s

            closedList[s.y][s.x] = True

        temp = end
        path = []
        while (temp is not None):
            path.append(f'[{temp.y},{temp.x}]')
            temp = pi[temp]

        path.reverse()
        return path

    @staticmethod
    def DLS(startCell, arena, taxi, destinationSearch, k):
        closedList = []
        for _ in range(len(arena)):
            closedList.append([False] * len(arena[0]))

        openList = [startCell]
        pi = {startCell: None}
        end = None
        depth = {startCell: 0}

        while openList:
            s = openList.pop()
            if (not destinationSearch and s.client is not None):
                taxi.client = s.client
                taxi.x = s.x
                taxi.y = s.y

                s.client = None
                s.taxi = taxi

                startCell.taxi = None

                end = s
                break

            elif (destinationSearch and s.destination is not None
                  and taxi.client.id == s.destination.id):
                taxi.money += taxi.client.budget
                taxi.client = None
                taxi.x = s.x
                taxi.y = s.y

                end = s
                s.taxi = taxi
                s.destination = None

                startCell.taxi = None

                break
            
            if (depth[s] >= k):
                if (len(openList) == 0):
                    return False
                else:
                    continue

            neighbouringCells = s.getNeighbours(arena)
            for cell in neighbouringCells:
                if (closedList[cell.y][cell.x] == False):
                    openList.append(cell)
                    depth[cell] = depth[s] + 1
                    pi[cell] = s

            closedList[s.y][s.x] = True

        temp = end
        path = []
        while (temp is not None):
            path.append(f'[{temp.y},{temp.x}]')
            temp = pi[temp]

        path.reverse()
        return path

    @staticmethod
    def IDS(startCell, arena, taxi, destination):
        k = 1
        while True:
            path = SearchAlgorithms.DLS(startCell, arena, taxi, destination, k)
            if (path != [] and path != False):
                return path
            if (k > len(arena) * len(arena[0])):
                return []
            k = k + 1

    @staticmethod
    def RunAlgo(flavour, arena, taxi):
        
        allPaths = []

        destinationSearch = False

        while (True):
            startCell = arena[taxi.y][taxi.x]
            if (flavour == 'BFS'):
                path = SearchAlgorithms.BFS(startCell, arena, taxi, destinationSearch)

            if (flavour == 'UCS'):
                path = SearchAlgorithms.UCS(startCell, arena, taxi, destinationSearch)

            if (flavour == 'DFS'):
                path = SearchAlgorithms.DFS(startCell, arena, taxi, destinationSearch)

            if (flavour == 'DLS'):
                path = SearchAlgorithms.DLS(startCell, arena, taxi, destinationSearch, 9)

            if (flavour == 'IDS'):
                path = SearchAlgorithms.IDS(startCell, arena, taxi, destinationSearch)

            if (len(path) == 0):
                break
            else:
                print(path)
                IoHandler.PrintArena(arena)
                destinationSearch = not destinationSearch
                allPaths.append(path)
        return allPaths

    @staticmethod
    def DetermineSolution(paths, clients, destinations):
        print(paths)

        fuelUsed = 0
        actions = []
        ispickUpTrip = True
        
        for path in paths:
            if path is not None:
                fuelUsed += len(path)
            
                for i in range(len(path) - 1):
                    crtCell = eval(path[i])
                    nextCell = eval(path[i + 1])

                    if (ispickUpTrip):
                        crtx,crty = crtCell
                        if (any(client.starty == crty and client.startx == crtx) for client in clients)):


                    actions.append(SearchAlgorithms.GetDirection(crtCell, nextCell))
            ispickUpTrip = not ispickUpTrip

        return (actions, fuelUsed)

    @staticmethod
    def GetDirection(crt, nxt):
        y1,x1 = crt
        y2,x2 = nxt

        if y2 == y1 - 1:
            return NORTH
        elif y2 == y1 + 1:
            return SOUTH
        elif x2 == x1 + 1:
            return EAST
        elif x2 == x1 - 1:
            return WEST
        return "INVALID MOVE"
