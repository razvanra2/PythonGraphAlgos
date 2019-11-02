from iohandler import *
from SearchAlgorithms import *
from os import system
from time import sleep

def main():
    (arena, taxi) = IoHandler.ReadInputFile('input.txt')

    IoHandler.PrintArena(arena)

    output = SearchAlgorithms.RunBfs(arena, taxi)

if __name__ == "__main__":
    main()
