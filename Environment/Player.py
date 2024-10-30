import numpy as np
from typing import Tuple, List
import pickle
import os

class Player(object):
    def __init__(self, name: str, actionSize: int, symbol:int) -> None:
        '''
        Player Class define player behaviour and actions

        Name : String = Which Store either player is computer or human
        actionSize : Int [Array Size] = Size of the board and move that can be made
        alpha : ndarray = Prior Successes stored in the array
        beta : ndarray = Failures are stored in the array
        
        n: ndarray = count of the action selected
        '''

        self.alpha: np.ndarray = np.ones(actionSize)
        self.beta: np.ndarray = np.ones(actionSize)
        self.n : np.ndarray = np.zeros(actionSize)
        self.playerSymbol: int = symbol
        self.name: str = name

    def chooseAction(self, avaiable_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        """
        Implementation of the thompson sampling algorithm 

        input:
        Avaiable Postions is taken as a input in parameter
        """
        sampled_values = np.zeros(len(self.alpha))
    
        availableSpace = []
        for pos in avaiable_positions:
            availableSpace.append(self.actionIndex(pos))

        for i in availableSpace:
            sampled_values[i] = np.random.beta(self.alpha[i], self.beta[i])

        actionIndex = np.argmax(sampled_values)
        action = self.indexAction(actionIndex)
    
        self.n[actionIndex] += 1 
        return action

    def actionIndex(self, action):
        return action[0] * 3 + action[1]

    def indexAction(self, index):
        return divmod(index, 3)

    def rewardAgent(self, action: Tuple[int, int], reward: int):
        actionIndex = self.actionIndex(action)
        if reward == 1:
            self.alpha[actionIndex] += 1
        else:
            self.beta[actionIndex] += 1
        self.n[actionIndex] += 1

    def createPolicy(self, filename: str) -> str:
        model = {
            "alpha": self.alpha,
            "beta": self.beta
        }
        with open(filename, 'wb') as f:
            pickle.dump(model, f)
        return os.path.join(os.getcwd(), filename)

    def loadPolicy(self, filename: str):
        with open(filename, 'rb') as f:
            model = pickle.load(f)
        self.alpha = model["alpha"]
        self.beta = model["beta"]




class HumanAgent(Player):
    def __init__(self, symbol: int, actionSize: int) -> None:
        self.alpha: np.ndarray = np.ones(actionSize)
        self.beta: np.ndarray = np.ones(actionSize)
        self.n: np.ndarray = np.zeros(actionSize)

        self.playerSymbol: int = symbol

    def chooseAction(self, availablePositions: List[Tuple[int]]) -> Tuple[int]:
        """
        Gets input from keyboard
        """
        print("Available Position : ", availablePositions)
        while True:
            try:
                row = int(input("Enter the row [0, 1, 2] : "))
                col = int(input("Enter the Col [0, 1, 2] : "))
                action = (row, col)

                if action not in availablePositions:
                    print("Space has been occupied")
                else: 
                    return action
            except ValueError:
                print("Invalid input")