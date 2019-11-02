from MapObjects import *
import emoji
class IoHandler:
    @staticmethod
    def ReadInputFile(filename):
        fileReader = open(filename, "r")
    
        line = fileReader.readline()
        height = int(line.split(" ")[0])
        width = int(line.split(" ")[1])
        capacity = int(line.split(" ")[2])

        arena = []
        for i in range(height):
            arenaLine = []
            for j in range(width):
                arenaLine.append(Cell(j, i))
            arena.append(arenaLine)


        line = fileReader.readline()
        cary = int(line.split(" ")[0])
        carx = int(line.split(" ")[1])

        taxi = Taxi(carx, cary, capacity)
        arena[cary][carx].taxi = taxi

        clientsCount = int(fileReader.readline())
        for i in range(clientsCount):
            clientLineToks = fileReader.readline().split(" ")
            starty = int(clientLineToks[0])
            startx = int(clientLineToks[1])
            endy = int(clientLineToks[2])
            endx = int(clientLineToks[3])
            budget = int(clientLineToks[4])

            client = Client(starty, startx, budget, i)
            destination = Destination(endx, endy, i)

            (arena[starty][startx]).client = client
            (arena[endy][endx]).destination = destination
        fileReader.readline()
        for i in range(height):
            line = fileReader.readline().rstrip('\n')
            separators = line.split(' ')

            for j in range(width):
                westSeparator = separators[j]
                eastSeparator = separators[j + 1]

                if (i != 0):
                    arena[i][j].directions.append(NORTH)
                if (i != height - 1):
                    arena[i][j].directions.append(SOUTH)
                if (westSeparator == ':'):
                    arena[i][j].directions.append(WEST)
                if (eastSeparator == ':'):
                    arena[i][j].directions.append(EAST)
        fileReader.close()
        return (arena,taxi)
    @staticmethod
    def PrintOutput(strategy, time, states, cost, solution):
        fileWriter = open(f'{strategy}_output.txt', "w")

        fileWriter.write(f'{strategy}\n')
        fileWriter.write(f'{time}\n')
        fileWriter.write(f'{states}\n')
        fileWriter.write(f'{cost}\n')
        fileWriter.write(f'{solution}\n')

        fileWriter.close()

    @staticmethod
    def GetArenaChar(cell):
        if (cell.taxi != None):
            return emoji.emojize(':oncoming_taxi:')
            return 'T'
        elif (cell.destination != None):
            return emoji.emojize(':thumbs_up:')
            #return 'D'
        elif (cell.client != None):
            return emoji.emojize(':boy:')
            #return 'C'
        return ' '

    @staticmethod
    def PrintArena(arena):
        height = len(arena)
        width = len(arena[0])

        topBottomLine = '+'
        for _ in range(2*width - 1):
            topBottomLine += '-'
        topBottomLine += '+'

        print(topBottomLine)
        for i in range(height):
            lineString = ''
            for j in range(width):
                if (WEST in arena[i][j].directions and j != width - 1):
                    lineString += (f':{IoHandler.GetArenaChar(arena[i][j])}')
                elif (WEST not in arena[i][j].directions and j != width - 1):
                    lineString += (f'|{IoHandler.GetArenaChar(arena[i][j])}')
                elif (WEST in arena[i][j].directions and j == width - 1):
                    lineString += (f':{IoHandler.GetArenaChar(arena[i][j])}|')
                elif (j == width - 1):
                    lineString += (f'|{IoHandler.GetArenaChar(arena[i][j])}|')
            print(lineString)
        print(topBottomLine)
