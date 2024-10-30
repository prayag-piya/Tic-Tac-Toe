import numpy as np
from typing import Tuple, List

BOARD_ROW = 3
BOARD_COL = 3

class Board(object):
    def __init__(self, p1, p2) -> None:
        '''
        This constructor init the empty board and two players
        '''
        self.p1 = p1
        self.p2 = p2
        self.board = np.zeros((BOARD_ROW, BOARD_COL))
        
        self.gameLoop = True
    
    def winningCondition(self) -> int: 
        '''
        winningCondition is implemented to check any winning condition
        Function return the player Id which is either 1 or -1 
        the checker function is called after each iteration of the player step
        '''
        for i in range(BOARD_COL-1):
            col: np.ndarray = self.board[i, :]
            
            if sum(col) == 3:
                self.gameLoop = False
                return 1
            if sum(col) == -3:
                self.gameLoop = False
                return -1
            row: np.ndarray = self.board[:, i]
            
            if sum(row) == 3:
                self.gameLoop = False
                return 1
            if sum(row) == -3:
                self.gameLoop = False
                return -1
            
        # this are diagonal check 
        diagonal_one: int = sum(np.diag(self.board))
        diagonal_two: int = sum(np.diag(np.fliplr(self.board)))
        
        diagonal:int = max(abs(diagonal_one), abs(diagonal_two))
        if diagonal == 3:
            self.gameLoop = False
            if (diagonal_one == 3) | (diagonal_two == 3):
                return 1
            else:
                return -1
            
        #Checking for Tie Condition
        emptyPosition: list = self.emptySpace()
        if (len(emptyPosition)) == 0:
            self.gameLoop = False
            return 0

        self.gameLoop = True
        return 2

    def updateBox(self, position:Tuple[int, int], playerSymbol:int) -> None:
        """
        Update the position of the box
        """
        if self.board[position] == 0:
            self.board[position] = playerSymbol
        else:
            print("Place already occupied")
        

    def emptySpace(self) -> List[Tuple[int, int]]:
        '''
        Checks for aviable space in the board
        '''
        space = []
        for i in range(BOARD_ROW):
            for j in range(BOARD_COL):
                if self.board[i, j] == 0:
                    space.append((i, j))
        return space


    def render(self) -> None:
        """
        Function renders the board in the terminal,
        Will Update to pygame later
        """
        for i in range(BOARD_ROW):
            print("--------------")
            border = "|  "
            for j in range(BOARD_COL):
                if self.board[i][j] == 0:
                    border += "  | "
                if self.board[i][j] == 1:
                    border += "X | "
                if self.board[i][j] == -1:
                    border += "0 | "
            print(border)
        print("--------------")

    def mainLoop(self):
        currentPlayer = self.p1
        opponent = self.p2
        while self.gameLoop:
            availableSpace: List[Tuple[int, int]] = self.emptySpace()
            if len(availableSpace) <= 0:
                print("It's a tie")
                self.p1.rewardAgent((-1, -1), 0)
                self.p2.rewardAgent((-1, -1), 0)
                self.gameLoop = False
                break
            action: Tuple[int, int] = currentPlayer.chooseAction(availableSpace)
            if action not in availableSpace:
                print(f"Invalid action taken: {action}. Try again")
                continue
            if action in availableSpace:
                self.updateBox(action, currentPlayer.playerSymbol)
                self.render()
                checkWinners: int = self.winningCondition()
                if checkWinners != 2:
                    if checkWinners == 1:
                        print("Player 1 Wins")
                        self.p1.rewardAgent(action, checkWinners)
                        self.p2.rewardAgent(action, -checkWinners)
                    elif checkWinners == -1:
                        print("PPlayer 2 Wins")
                        self.p1.rewardAgent(action, checkWinners)
                        self.p2.rewardAgent(action, -checkWinners)

                    elif checkWinners == 0:
                        print("It's a tie")
                        self.p1.rewardAgent(action, checkWinners)
                        self.p2.rewardAgent(action, -checkWinners)
                    self.gameLoop = False
                    break
                currentPlayer, opponent = opponent, currentPlayer
            else:
                print("Invalid action taken, Try again")