# Matthew Petersen
#  4-7-2025
# Lab Week 12
# 
# Description : 
# 
# 
# 


import pytest
from fourInSequence import checkForNextMoveWin, checkAdjacent, checkDraw, checkWinner

def test_checkForNextMoveWin():
    board = [
        ['X', 'O', ' '],
        ['X', 'O', ' '],
        ['X', ' ', ' ']
    ]
    result = checkForNextMoveWin(board, 'X')
    assert result == True, "Test failed: Player X should be able to win in the next move."


def test_checkAdjacent():
    board = [
        ['X', 'X', 'O'],
        [' ', 'X', ' '],
        ['O', ' ', ' ']
    ]
    result = checkAdjacent(board, 'X')
    assert result == True, "Test failed: There should be adjacent 'X' pieces."


def test_checkDraw():
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    result = checkDraw(board)
    assert result == True, "Test failed: The game should be a draw."
    
    board = [
        ['X', 'O', 'X'],
        ['O', 'X', ' '],
        ['O', 'X', 'O']
    ]
    result = checkDraw(board)
    assert result == False, "Test failed: The game is not a draw yet."


def test_checkWinner():
    board = [
        ['X', 'X', 'X', ' '],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ]
    result = checkWinner(board, 'X')
    assert result == True, "Test failed: X should be the winner."

    board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['X', 'O', 'X']
    ]
    result = checkWinner(board, 'X')
    assert result == False, "Test failed: There should be no winner for player X."
    
    result = checkWinner(board, 'O')
    assert result == False, "Test failed: There should be no winner for player O."


