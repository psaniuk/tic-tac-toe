from datetime import datetime
from collections import defaultdict

class NoMovesAvailableException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
class Game:
    def __init__(self, gridSize: int) -> None:
        self.__grid = Grid(gridSize)
        self.__playerX = Player.createXplayer()
        self.__playerO = Player.createOplayer()
        self.__currentPlayer = None
        self.__movesCounter = gridSize * gridSize
    
    def play(self, newMove):
        if self.__movesCounter == 0:
            raise NoMovesAvailableException()
        
        if not self.__currentPlayer:
            self.__currentPlayer = self.__playerO if datetime.now().second % 2 else self.__playerX

        row = newMove // 3
        col = newMove % 3
        self.__grid.move(self.__currentPlayer, row, col)
        self.__movesCounter -= 1
        self.__currentPlayer = self.__playerO if self.__currentPlayer is self.__playerX else self.__playerX

    def isCompleted(self):
        return self.__movesCounter == 0 or self.getWinner() is not None
    
    def getWinner(self):
        return self.__grid.getWinner()
    
    def getResult(self):
        return self.__grid.getCells()
    
class Player:
    def __init__(self, mark) -> None:
        self.__mark = mark
    
    def getMark(self):
        return self.__mark
    
    def createXplayer():
        return Player("X")
    
    def createOplayer():
        return Player("O")
    
class Grid:
    def __init__(self, size) -> None:
        self.__grid = [[None for _ in range(size)] for _ in range(size)]
    
    def move(self, player: Player, row: int, col: int):
        self.__grid[row][col] = player
    
    def getWinner(self):    
        def checkCounters(counters):
            for player, count in counters.items():
                if count == len(self.__grid):
                    return player
            return None

        def getWinner(hashtable):
            for _, counters in hashtable.items():
                if len(counters.items()) > 1:
                    continue
                winner = checkCounters(counters)
                if winner:
                    return winner
            return None         
        
        rowsDict, colsDict = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: defaultdict(int))
        primaryDiagonalDict, secondaryDiagonalDict = defaultdict(int), defaultdict(int)

        for row in range(len(self.__grid)):
            primaryDiagonalDict[self.__grid[row][row]] += 1
            secondaryDiagonalDict[self.__grid[row][len(self.__grid) - row - 1]] += 1

            for col in range(len(self.__grid[row])):
                player = self.__grid[row][col]
                if not player:
                    continue
                
                rowsDict[row][player] += 1
                colsDict[col][player] += 1
                     
        return (
            getWinner(rowsDict) or
            getWinner(colsDict) or
            checkCounters(primaryDiagonalDict) or
            checkCounters(secondaryDiagonalDict)
        )
  
    
    def getCells(self):
        return [row[:] for row in self.__grid]




