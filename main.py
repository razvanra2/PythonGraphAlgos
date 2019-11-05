from iohandler import *
from SearchAlgorithms import *
from os import system
from time import sleep
import copy

def main():
    (arena, taxi, clients, destinations) = IoHandler.ReadInputFile('input.txt')

    IoHandler.PrintArena(arena)

    output = SearchAlgorithms.RunAlgo('IDS', arena, taxi)

    solution = SearchAlgorithms.DetermineSolution(output,
        copy.deepcopy(clients), copy.deepcopy(destinations))
    print(solution)

if __name__ == "__main__":
    main()
