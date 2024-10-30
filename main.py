from Environment.Board import Board, BOARD_COL, BOARD_ROW
from Environment.Player import Player, HumanAgent
import argparse

def save_agents_policy(p1: Player, p2: Player, p1_filename: str, p2_filename: str):
    p1.createPolicy(p1_filename)
    p2.createPolicy(p2_filename)
    print(f"Policies saved to {p1_filename} and {p2_filename}")


def traning(epoch: int, p1: Player, p2: Player):
    for i in range(epoch):
        game = Board(p1, p2)
        game.mainLoop()
        if i % 1000 == 0:
            print(f"Completed {i} games")
    save_agents_policy(p1, p2, f"p1_policy.pkl", f"p2_policy.pkl")

def testing(filepath: str, p1: Player, p2: Player):

    p1.loadPolicy(filepath)

    game = Board(p1, p2)
    game.mainLoop()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--training", help="it will start a training process and save ")
    parser.add_argument("--testing", help="human interface will pop up for playing with trained agent")
    parser.add_argument("--policy", help="file path of policy")
    parser.add_argument("--epoch", help="number of to train the agent", type=int)
    args = parser.parse_args()
    if args.training:
        if args.epoch > 0:
            p1 = Player("Player 1", actionSize=BOARD_ROW * BOARD_COL, symbol=1)
            p2 = Player("Player 2", actionSize=BOARD_ROW * BOARD_COL, symbol=-1)
            NUM_GAMES = args.epoch 
            traning(NUM_GAMES, p1, p2)
        else:
            print("provide a number for traning the agent [--epoch 50000]")
    
    elif args.testing: 
        if args.policy:
            p1 = Player("Player 1", actionSize=BOARD_ROW * BOARD_COL, symbol=1)
            p2 = HumanAgent(symbol=-1, actionSize=BOARD_ROW * BOARD_COL)
            testing(args.policy, p1, p2)
        else:
            print("No Policy flie were set [--policy p1_policy.pkl]")
    else:
        print("Turn on testing | training [--testing 1 | --training 1]")

main()