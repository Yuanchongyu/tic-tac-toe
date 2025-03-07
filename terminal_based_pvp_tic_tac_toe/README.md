# Tic Tac Toe (Terminal Two-Player Game)

This is a simple Tic Tac Toe game implemented in Python that allows two players to play against each other in the terminal. The game uses a 3x3 board where players take turns to place their mark (either **X** or **O**). The first player to align three marks (horizontally, vertically, or diagonally) wins the game; if the board fills up without any winning combination, the game ends in a draw.

## Features

- **Terminal-based**: Run the game in a terminal or command prompt.
- **Two-player mode**: Supports two players playing on the same machine.
- **Input validation**: Checks for invalid or duplicate moves.
- **Win detection**: Automatically determines if X or O wins, or if the game is a draw.

## Requirements

- Python 3.x

No additional external libraries are required since the code uses only Python's standard library functions.

## How to Run


1. **Open a Terminal or Command Prompt**

2. **Navigate to the Directory**

   Use `cd` to change to the directory where `tic_tac_toe.py` is located.

3. **Run the Script**

   Execute the following command:
   
   ```bash
   python tic_tac_toe.py
   ```

4. **Play the Game**

   Follow the on-screen instructions to play the game. Input a number (1-9) corresponding to the board position where you want to place your mark.

## Future Enhancements

In later lessons, we will expand this project by:
- Adding a graphical user interface (GUI) using libraries like Tkinter or Pygame.
- Introducing AI opponents using various algorithms:
  - Random move selection (baseline)
  - Minimax algorithm (with and without alpha-beta pruning)
  - Monte Carlo Tree Search (MCTS)
  - Reinforcement Learning (e.g., Q-Learning, Policy Gradient)
- Comparing the performance and strategy quality of these algorithms.

## License

This project is open source. Feel free to use and modify the code for educational purposes.

---

Enjoy playing and learning!
