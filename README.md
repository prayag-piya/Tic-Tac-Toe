# Tic-Tac-Toe with Thompson Sampling Strategy
This project explores a probabilistic algorithm to strategize winning moves in a Tic-Tac-Toe game using the Thompson Sampling algorithm. Thompson Sampling is widely used in decision-making under uncertainty, especially in multi-armed bandit problems. Here, the algorithm allows the agent to learn a winning strategy by balancing exploration and exploitation during gameplay.

## Project Structure
The project consists of the following files:

- **Board.py**: Contains the Tic-Tac-Toe board environment setup, functions to check for available positions, determine the winner, and render the board.
- **Player.py**: Defines the player class and behaviors, implementing the Thompson Sampling algorithm to optimize moves.
- **Main.py**: Integrates the environment and player classes for running training and testing phases.

## Algorithm Overview
The Thompson Sampling algorithm operates by maintaining a probability distribution for the expected reward of each possible action:

- **Initialization**: For each action, initialize a prior distribution for expected rewards using a beta distribution with alpha (success) and beta (failure) parameters.
- **Action Selection**: Sample a reward from each action's distribution, selecting the action with the highest reward.
- **Reward Observation**: Execute the chosen action, observe the reward, and update the beta distribution accordingly.
- **Repeat**: The algorithm iterates until it balances between exploration and exploitation, optimizing its moves.

## Key Features
- **Training**: Train the agent on the Tic-Tac-Toe environment with Thompson Sampling using binary rewards.
- **Testing**: Load a trained model and test it against a human agent.
Human-Agent Gameplay: A Human Agent class inherits from the Player class, allowing human-vs-agent gameplay.

## Setup and Installation

### Clone the repository:
```
git clone https://github.com/yourusername/tic-tac-toe-thompson-sampling.git
cd tic-tac-toe-thompson-sampling
```

### Install dependencies
This project uses ```numpy``` and ```pickle```. Install dependencies via pip:
```
pip install -r requirement.txt
```
# Usage
### Training the Model
To train the agent, use the ```--training``` and ```--epoch``` arguments:
```
python main.py --training 1 --epoch 10000
```
- **--training**: Set to 1 to initiate the training process.
- **--epoch**: Specifies the number of training iterations (e.g., 10,000).

### Testing the Model
To test a trained model against a human player, use the ```--testing``` and ```--policy``` arguments:

```
python Main.py --testing 1 --policy saved_model.pkl
```
- **--testing**: Set to 1 to initiate the testing process.
- **--policy**: Specifies the path to the saved model file (e.g., saved_model.pkl).
  
# Observed Results
After training the agent with Thompson Sampling:

- The agent tends to exploit successful moves, with winning strategies concentrating on specific columns or rows after 50,000 training iterations.
- A bias towards exploiting certain moves suggests limited exploration but effective exploitation in repetitive scenarios.

# Contributions
Feel free to contribute by improving exploration strategies, visualizing gameplay, or adding features. Fork the repository, create a branch, and submit a pull request!
