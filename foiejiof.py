import random
import sys

def printTitleMaterial():
    print("Four in seguence")
    print()
    print("By: Matthew Petersen")
    print("COMS Section C ")

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
        
        return choice
    
def chooseNumPlayers():
    while True:
        try:
            num_players = int(input("Number of Players? [1] / [2]: "))
            if num_players in [1, 2]:
                return num_players
            else:
                print("ERROR: Please enter either 1 or 2...")
        except ValueError:
            print("ERROR: Please enter a valid number (1 or 2)...")

def print_banner():
    print("###########################################")
    print()
    print("Starting First Round!")
    print()

def get_player_piece(player_number):
    if player_number == 0:
        return "."
    elif player_number == 1:
        return "X"
    elif player_number == 2:
        return "O"
    return ""

def create_board(width, height):
    empty = get_player_piece(0)
    board = []
    for i in range(height):
        row = [empty] * width
        board.append(row)
    return board


def print_board(board):
    for row in board:
        for column in row:
            print(column, end="")
            print()
    for i in range(len(board[0])):
        print(i, end="")
        print()
        print()

def get_column_int(board, player_number):
    return int(input("Player {0}, please select a column between (0-{1}): ".format(player_number, len(board[0]) - 1)))

def get_input_in_range(board, player_number):
    col = get_column_int(board, player_number)

    while col < 0 or col > len(board[0]) - 1:
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = get_column_int(board, player_number)
    
    return col


def get_open_row():

    def get_human_input(board, player_number):
        col = get_input_in_range(board, player_number)
        while get_open_row(board, col) == -1:
            print("ERROR: Column {0} is full! Please choose a different column...".format(col))
            col = get_input_in_range(board, player_number)
            
        return col
    
def check_for_next_move_win(board, player_number):
    empty = get_player_piece(0)  
    piece = get_player_piece(player_number)  

    for col in range(len(board[0])):
        
        row = get_open_row(board, col)  
        
        if row != -1:
            place_piece(board, row, col, piece) 
            
            if check_winner(board, player_number):
                place_piece(board, row, col, empty)  
                return col  
            
            place_piece(board, row, col, empty)
    
    return -1
