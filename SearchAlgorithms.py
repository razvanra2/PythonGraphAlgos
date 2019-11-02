from MapObjects import *
from iohandler import *

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
    def RunBfs(arena, taxi):
        
        allPaths = []

        destinationSearch = False

        while (True):
            startCell = arena[taxi.y][taxi.x]
            path = SearchAlgorithms.BFS(startCell, arena, taxi, destinationSearch)
            
            if (len(path) == 0):
                break
            else:
                print(path)
                IoHandler.PrintArena(arena)
                destinationSearch = not destinationSearch



