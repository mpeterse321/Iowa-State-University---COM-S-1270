# Matthew Petersen
# 3-24-25
# Assignment 4
# 
# Description: In this code you will be playing connect four against the computor. 
# Player #1 (You) will be X and the computer will be 0. The concept of this game 
# is to beet the computer on this 6x6 grid. GOODLUCK!
#

import copy

def checkForNextMoveWin(board, player):

    rows = len(board)
    cols = len(board[0])

    # Check each column
    for col in range(cols):
        for row in range(rows - 1, -1, -1):  # Check from the bottom of the column
            if board[row][col] == ' ':
                # Simulate placing the piece
                board[row][col] = player

                # Check if this move results in a win
                if checkWinner(board, player):  # This function checks for a win
                    board[row][col] = ' '  # Undo the move
                    return True  # Player can win with this move

                # Undo the move if it's not a win
                board[row][col] = ' '
                break  # Break after checking one empty spot in the column

    return False  # No winning move found


def checkAdjacent(board, player):
    rows = len(board)
    cols = len(board[0])

    # Horizontal Check
    for row in range(rows):
        for col in range(cols - 1):  # Only check up to the second-to-last column
            if board[row][col] == player and board[row][col + 1] == player:
                return True

    # Vertical Check
    for row in range(rows - 1):  # Only check up to the second-to-last row
        for col in range(cols):
            if board[row][col] == player and board[row + 1][col] == player:
                return True

    # Diagonal (top-left to bottom-right) Check
    for row in range(rows - 1):  # Only check up to the second-to-last row
        for col in range(cols - 1):  # Only check up to the second-to-last column
            if board[row][col] == player and board[row + 1][col + 1] == player:
                return True

    # Diagonal (top-right to bottom-left) Check
    for row in range(rows - 1):  # Only check up to the second-to-last row
        for col in range(1, cols):  # Only check up to the second-to-last column
            if board[row][col] == player and board[row + 1][col - 1] == player:
                return True

    return False  # No adjacent pieces found


def checkWinner(board, player):

    rows = len(board)
    cols = len(board[0])

    # Check horizontal lines
    for row in range(rows):
        for col in range(cols - 3):  # Only check up to the 4th column
            if board[row][col] == player and board[row][col + 1] == player and \
               board[row][col + 2] == player and board[row][col + 3] == player:
                return True  # Found 4 in a row horizontally

    # Check vertical lines
    for row in range(rows - 3):  # Only check up to the 4th row
        for col in range(cols):
            if board[row][col] == player and board[row + 1][col] == player and \
               board[row + 2][col] == player and board[row + 3][col] == player:
                return True  # Found 4 in a column vertically

    # Check diagonals (top-left to bottom-right)
    for row in range(rows - 3):  # Only check up to the 4th row
        for col in range(cols - 3):  # Only check up to the 4th column
            if board[row][col] == player and board[row + 1][col + 1] == player and \
               board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True  # Found 4 in a diagonal (top-left to bottom-right)

    # Check diagonals (top-right to bottom-left)
    for row in range(rows - 3):  # Only check up to the 4th row
        for col in range(3, cols):  # Only check columns where there's room for a diagonal
            if board[row][col] == player and board[row + 1][col - 1] == player and \
               board[row + 2][col - 2] == player and board[row + 3][col - 3] == player:
                return True  # Found 4 in a diagonal (top-right to bottom-left)

    return False  # No winner found


def checkDraw(board):
    """
    Checks if the game has ended in a draw (full board, no winner).
    """
    rows = len(board)
    cols = len(board[0])

    # Check if the board is full
    for row in board:
        if ' ' in row:  # If there is an empty space, it's not a draw
            return False

    # Check if there is no winner
    if not checkWinner(board, 'X') and not checkWinner(board, 'O'):
        return True  # It's a draw if the board is full and there is no winner

    return False  # Not a draw if there is a winner
 # ----------------------------------------

# I DONT KNOW HOW TO DO THIS AND I AM ABOUT TO CRAHSOUT.