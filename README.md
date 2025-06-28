# 🧠 Tic-Tac-Toe with Classic AI (Minimax Algorithm)

This project implements a fully functional and unbeatable **Tic-Tac-Toe AI** using the **Minimax algorithm**, a classical approach in Artificial Intelligence for making optimal decisions in turn-based games.

The visual interface is built using **Pygame**, and the logic behind the AI is constructed with plain Python and the standard `math` module — no external AI libraries required.

## 📂 Project Structure

- `tictactoe.py`  
  Contains the complete game logic:
  - Board representation
  - Move validation
  - Win conditions
  - Terminal state checks
  - The **Minimax algorithm** for optimal AI decision-making

- `runner.py`  
  Responsible for rendering the game interface using Pygame and managing user interaction.

## How to Run

1. **Install the required library:**

```
pip install pygame
python runner.py
```

Choose to play as X or O and face the AI — which will never lose.

## About the Minimax Algorithm
Minimax is a recursive decision-making algorithm used for minimizing the possible loss for a worst-case scenario. In this game:

X is the maximizing player

O is the minimizing player

The AI explores the full game tree and chooses the optimal move based on utility values:

+1 for a win by X

-1 for a win by O

0 for a draw

## Author
Developed by Leonardo Vianna
Feel free to reach out or contribute!

📌 Educational use only. Ideal for those learning about game theory, classic AI algorithms, and Python application development.
