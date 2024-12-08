# Tic-Tac-Toe
<div align="center">
<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGdybHF5aHQ1NGxvbjh6Mm8xM2V0ZW51ZWJmNXR5ejlldmcxNWhmeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gR92EF4p9XyEHyD2n5/giphy.gif" alt="Figure 0: Cover Image" width="300">
</div>

⚖  _GIF Credits: [Giphy Link](https://giphy.com/gifs/WarChildNorthAmerica-tic-tictactoe-tac-toe-gR92EF4p9XyEHyD2n5)_
# 🔖Table of Contents
1. [Introduction](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#introduction)
    - [Objectives](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#objectives)
    - [Prerequisites](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#prerequisites)
    - [Repository Guide](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#repository-guide)
2. [Guide & Features](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#-guide--features)
    - [Overview](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#overview)
    - [Configuration](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#configuration)
    - [Usage](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#usage)
3. [Known Issues and Future Plans](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#known-issues-and-future-plans)
    - [Known Issues](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#known-issues)
    - [Future Plans](https://github.com/NullPointerHQ/TicTacToePythonEdition/blob/main/README.md#future-plans)
## 👋Introduction
### Objectives
This project has the following objectives:
1. To simulate a two player game of TicTacToe
2. To allow me to learn more about Python via a more complex program. 
### Prerequisites 
1. Python Version 3.9
2. IDE:[Microsoft's Visual Studio](https://visualstudio.microsoft.com/#vs-section) or an IDE of your preference
3. Python's `random` Library
    - Used to randomly decide who gets to be X or O

Future Prerequisite: Python's `tkinter` Library
    - I plan on learning how this library works and rereleasing this software with an actual GUI interface.
### Repository Guide
You are currently viewing the README, there are two other files that will be of interest to you:
1. [Source Code](TicTacToe.py)
    - This is the source code file for the game itself.
2. [Save Game File](TTTGAMESTATE.txt)
    - This is a pre-generated save game file.
## 🎮 Guide & Features
### Overview
The program will begin by performing basic setup for the game:
1. Create two dictionaries to hold player information.
    - Both dictionaries hold the same key/value pair: `player_name` and  `player_icon`.
    - These fields will hold default values initially.
2. Create a list of lists `grid_details` to represent the grid squares.
3. Set up `current_player` used for taking turns. Hardcoded to start at 1, alternates between 1 and 2
4. Set up `end_game`, a flag variable which triggers the end of the game, and displays the winner.
5. Display a menu to the user and await their input

At this point, the user(s) can decide to either start a brand new game or continue one where they left off.

If the user(s) select 'New Game', the function `profile_setup(...)` is called, which will:
1. Randomly assign each player an icon (X or O)
2. Prompt the user for a name for Player 1 and then Player 2
3. Display the received Player names and their respective icons 

If the user(s) select 'Load Game', the `quickload(...)` function is called, which will look for a saved game file, an example file can be seen by clicking the second link in the repository guide section.

Either way, the next step for the program is to call `tictactoe`, this function does the following:
1. Calls `board_generator(grid_details)`
    - Displays the game board to the user.
    - Uses `grid_details` to determine where a user has made a move.
2. `WHILE` Loop initiates that repeats the process until a winner is found or a draw occurs:
    1. Inform the player's whose turn it is.
    2. Call the function `victory_checker`, check if the current player won the game
    3. Call `move_maker` to allow the player to make a move
          - `move_maker` checks validity of any moves using `valid_move`
    4. Call `quicksave` to save the current state of the board
    5. Set the value of `current_player` to the next player's value (e.g Set it to 2 if player 1 just went)
    6. Call `board_generator` to display the board
    7. No winner found? Return to step 2.1
3. Return `end_game`

 Once `tictactoe` returns the winner is displayed.
### Configuration
TicTacToe is fairly standard, there are not many options for what you can change:
1. You can modify the save files at any point, it is just a `.txt` file, the save file lets you modify:
    1. Player 1's information
    2. Player 2's information
    3. The current details of the board
2. The name of your save data, locate the line:  `with open("TTTGAMESTATE.txt", "w") as data:` in `quicksave` and `with open("TTTGAMESTATE.txt", "r") as data:` in `quickload` and change the `TTTGAMESTATE.txt`
portion, be sure that the lines match!
### Usage
1. Run the game in your preferred IDE, assuming you meet the prerequisites.
2. Enter either `1` or `2` for your preferred option
    1. **FOR A NEW GAME:** When prompted enter: `1`
          1. Enter Player 1's Name (e.g 'John Doe').
          2. Enter Player 2's Name (e.g Jane Doe).
    2. **TO LOAD A GAME:** When prompted enter: `2`
          1. The system will automatically load the information if the file exists, otherwise refer to _New Game_ instructions
3. The system will automatically tell you whose turn it is, use the Cartesian (X,Y) coordinate system to make a move.

## 💭Known Issues and Future Plans
### 💢Known Issues
- `You have tripped the Error Catcher!` may trigger at the start of gameplay
    - Cause: Unknown
    - Severity: Minor, does not affect gameplay.
### 🔮Future Plans
- Rewrite `victory_checker` to be much more efficient with some loops
- Rewrite the calls to `victory_checker` to check after a player has made a move
- Unknown degree of changes required to accommodate `tkinter` GUI
