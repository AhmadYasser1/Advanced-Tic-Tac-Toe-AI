# Advanced Tic-Tac-Toe AI: A Study in Adversarial Search

Welcome to the Advanced Tic-Tac-Toe AI project! This project showcases the implementation of a Tic-Tac-Toe game using various AI algorithms to create intelligent agents capable of strategic decision-making. The game features three levels of AI difficulty, each employing different techniques to enhance the gameplay experience.

## Project Description

This project is part of the Introduction to Artificial Intelligence course at the Egypt University of Informatics. The objective is to develop an AI-driven Tic-Tac-Toe game that can play against a human player with varying levels of difficulty, each demonstrating a different facet of artificial intelligence.

### Key Features

1. **Random Move Agent**: 
   - The AI performs legal moves randomly.
   - Serves as the baseline functionality, ensuring the agent adheres to the game rules.

2. **Minimax Algorithm**: 
   - Implements the Minimax algorithm for strategic decision-making.
   - The AI maximizes its own moves while minimizing the opponent's, providing a more challenging gameplay experience.

3. **Alpha-Beta Pruning**: 
   - Enhances the Minimax algorithm with Alpha-Beta Pruning.
   - Significantly improves the AI's efficiency, allowing for faster and more intelligent decision-making.

### Environment Classification

- **Fully Observable**: The entire game state is visible to both players.
- **Static**: The game rules and board structure remain constant.
- **Discrete**: A finite set of possible states and actions.
- **Known**: Well-defined rules govern legal moves and win conditions.
- **Multi-Agent**: Involves two players with distinct goals.
- **Sequential**: Players take alternating actions in a turn-based manner.
- **Deterministic**: Each action leads to a predictable outcome without randomness.

## Project Structure

- `game.py`: Contains the core game logic and AI implementations.
- `test_game.py`: Includes test cases for validating the AI algorithms.
- `tic_tac_toe.py`: Implements the game board and user interaction logic.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AhmadYasser1/advanced-tic-tac-toe-ai.git
   cd advanced-tic-tac-toe-ai

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   
3. **Run the game**:
   ```bash
   python tic_tac_toe.py

## Testing

1. **Run the test cases using pytest to ensure the correctness and efficiency of the AI algorithms:**
   ```bash
   pytest test_game.py

## Future Work

Future enhancements may include integrating depth limitation with alpha-beta pruning to further reduce computational complexity and improve efficiency for real-time applications.

## Authors

- **Ahmed Yasser Hassanein**
- **Malak Ahmed Raafat**
- **Omar Mohamed Elabasery**
- **Malak Mohamed Ibrahim**

## Supervisors

- **Dr. Mohamed Taher ElRefaei**
- **Dr. Farid Zaki**
- **Eng. Nadine ElSaeed**

## Acknowledgments

We would like to thank our course instructors and supervisors for their guidance and support throughout this project.
