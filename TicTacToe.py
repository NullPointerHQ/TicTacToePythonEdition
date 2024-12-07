#Objective: To make a functioning rendition of TicTacToe with 2 player control,save games, randomized pieces and a visual board
#Random Libraries or what have you
import random #Used in initial profile setup

#Function Definition Section

#Sets up player information
def profile_setup(player1_information, player2_information):
    #Picking Whos Who at random
    random.seed(42)#Seeds RNG Machine
    coin_flip = random.randint(0 , 1)#Generates a Random Integer between 0 and 1

    if (coin_flip == 0):
        player1_information['player_icon'] = 'X'
        player2_information['player_icon'] = 'O'
    else:
        player1_information['player_icon'] = 'O'
        player2_information['player_icon'] = 'X'

    #Gathers the Names
    player1_information['player_name'] = input("Enter Player 1's Name: ")
    player2_information['player_name'] = input("Enter Player 2's Name: ")

    #Displays the Player Info
    print(player1_information['player_name'], " will be ", player1_information['player_icon'], end=' ')
    print(" and ", player2_information['player_name'], " will be ", player2_information['player_icon'])
    return

#Handles displaying the board
def board_generator(grid_details):
    print("   |  0 |  1 |  2 |")#Prints a horizontal coordinate guide for the user's convinience
    print("-------------------")#Adds a vertical bar
    for i in range(3):#Handles the X coordinate
        print(i, " |", end="")#Prints a vertical coordinate guide for the user's convenience
        
        for j in range(3):#Handles the Y coordinate
            print(" ", grid_details[i][j], end=" |")#Will print the value at the coordinate and format it for the next
        print("\n-------------------")#Adds a vertical bar
            
    return

#Handles making moves on the board, Expects to be given the grid and the current player
def move_maker (grid_details, current_player_information):
    #Boolean Variable that checks if a vaild move has been made
    valid_move = False

    while(valid_move != True):
        #Gathers the point coordinates
        X = int(input("Enter X: "))
        Y = int(input("Enter Y: "))
    
        #Applies the player's icon IF the spot is not occupied AND its in the grid 
        if (X in range (3) and Y in range (3) and grid_details[X][Y] ==  " "):
            grid_details[Y][X] = current_player_information['player_icon']
            valid_move = True #Sets Boolean variable to True ending the loop
        
        #Returns an error and requests reinput
        elif(X not in range (3) or Y not in range(3)):
            print("Out of range! Please restrict yourself to the 3x3 grid!")

        else:
            print("That spot is already occupied!")

    return

#Checks for a Victory
def victory_checker (grid_details, current_player_information):
    #Row and Column should have been done via a loop
    #Column 0
    if(grid_details[0][0] == current_player_information['player_icon'] and 
        grid_details[0][1] == current_player_information['player_icon'] and 
        grid_details[0][2] == current_player_information['player_icon']):
        return current_player_information['player_name'] 
    #Column 1
    if(grid_details[1][0] == current_player_information['player_icon'] and 
        grid_details[1][1] == current_player_information['player_icon'] and 
        grid_details[1][2] == current_player_information['player_icon']):
        return current_player_information['player_name']
    #Column 2
    if(grid_details[2][0] == current_player_information['player_icon'] and 
        grid_details[2][1] == current_player_information['player_icon'] and 
        grid_details[2][2] == current_player_information['player_icon']):
        return current_player_information['player_name']
    #Row 0
    if(grid_details[0][0] == current_player_information['player_icon'] and 
        grid_details[1][0] == current_player_information['player_icon'] and 
        grid_details[2][0] == current_player_information['player_icon']):
        return current_player_information['player_name']
    #Row 1
    if(grid_details[0][1] == current_player_information['player_icon'] and
        grid_details[1][1] == current_player_information['player_icon'] and 
        grid_details[2][1] == current_player_information['player_icon']):
        return current_player_information['player_name']
    #Row 2
    if(grid_details[0][2] == current_player_information['player_icon'] and 
        grid_details[1][2] == current_player_information['player_icon'] and 
        grid_details[2][2] == current_player_information['player_icon']):
        return current_player_information['player_name']
    #Left -> Right Diagonal
    if(grid_details[0][0] == current_player_information['player_icon'] and 
       grid_details[1][1] == current_player_information['player_icon'] and 
       grid_details[2][2] == current_player_information['player_icon']):
        return current_player_information['player_name']
    #Right -> Left Diagonal
    if(grid_details[2][2] == current_player_information['player_icon'] and 
       grid_details[1][1] == current_player_information['player_icon'] and 
       grid_details[2][0] == current_player_information['player_icon']):
        return current_player_information['player_name'] 
    else:
        return "No Winner!"

    #Handles Saving Games

#Handles Saving Games
def quicksave (grid, player1, player2, current):
    #Opens the saved data file in 'Write' mode and assigns operations to the savedata variable
    try:
        with open("TTTGAMESTATE.txt", "w") as data:
            data.write(player1['player_name'] + "|" + player1['player_icon'] + "|\n")
            data.write(player2['player_name'] + "|" + player2['player_icon'] + "|\n")
            data.write(current + "|\n")

            for i in range(3):
                for j in range(3):
                    #Will always write the value at the coordinates given on last column will skip a line
                    if (j != 2):
                        data.write(grid[i][j] + "|")
                    else:
                        data.write(grid[i][j] + "|\n")
            data.close()#Closes the File
    except OSError as e:
        print("Error when writing to disk!")
    return

def quickload (grid, player1, player2, current):
    try:
        with open("TTTGAMESTATE.txt", "r") as data:
            file = data.readlines() #Turns 'file' into a list with all the data
            player1['player_name'], player1['player_icon'], newlinedump = file[0].split("|")
            player2['player_name'], player2['player_icon'], newlinedump = file[1].split("|")
            current, newlinedump = file[2].split("|")
            for x in range (3):
                grid[x][0],grid[x][1],grid[x][2],newlinedump = file[3 + x].split("|")
    
    except OSError as e:
        print("Error when reading save game!")
    return

#Operates the actual game
def tictactoe(grid_details, player1_information,player2_information, current_player, end_game):
    board_generator(grid_details)#Generates the board for the first time
    while(end_game == "No Winner!"):
        if (current_player == "1" and end_game == "No Winner!"):
            print("It is: ", player1_information['player_name'], "'s turn!")#Tells the user whose turn it is
            end_game = victory_checker(grid_details, player1_information)#Checks for a win
            move_maker(grid_details, player1_information)#Calls the function for the player to make their move
            quicksave(grid_details, player1_information, player2_information, current_player)
            current_player = "2"#Passes the baton
            board_generator(grid_details)#Displays the board

        if (current_player == "2" and end_game == "No Winner!"):
            print("It is: ", player2_information['player_name'], "'s turn!")#Tells the user whose turn it is
            end_game = victory_checker(grid_details, player2_information)#Checks for a win
            move_maker(grid_details, player2_information)#Calls the function for the player to make their move
            current_player = "1"#Passes the baton
            board_generator(grid_details)#Displays the board
    
    return end_game

#Main Program
#Player Information Dictionaries
player1_information = { 'player_name' : 'PLAYER 1', 'player_icon' : '?' }
player2_information = { 'player_name' : 'PLAYER 2', 'player_icon' : '?' }

#Setting Up the Coordinate Grid
grid_details = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

#Creating the main menu

end_game = "No Winner!" #Just ensures that when a winner is found the game ends
current_player = "1" #Tracks whose turn it is
print("Tic Tac Toe!\n","==============\n","1) New Game!\n", "2) Load Game!")
choice = int(input("\nUSER: "))#Used for a sort of switch statement
while (end_game == "No Winner!"):

    if (choice == 1):
        print("New Game Selected.")
        profile_setup(player1_information, player2_information) #Sets up the player names and their icons
    if (choice == 2):
        print("Load Game Selected")
        quickload(grid_details, player1_information, player2_information, current_player)
    else:
        print("You have tripped the Error Catcher!")

    end_game = tictactoe(grid_details, player1_information, player2_information, current_player, end_game)#Calls the function that operates the game
print("Winner Found! Congratulations:", end_game)
 
