# Matthew Petersen
#  4-7-2025
# Lab Week 12
# 
# Description : This code we will be playing rock-paper-scissors against the computer.
# This code takes that game and tests it to make sure that there are no errors nor failures
# in the test to make sure that the code has passed.

import pytest
from rockPaperScissors import generateComputerMove, determineWinner, playRound
from unittest.mock import patch

def test_generateComputerMove():
    choices = ["Rock", "Paper", "Scissors"]
    result = generateComputerMove()
    assert result in choices

def test_determineWinner():
    assert determineWinner("Rock", "Paper") == "Paper"
    assert determineWinner("Paper", "Rock") == "Paper"
    assert determineWinner("Scissors", "Rock") == "Rock"
    assert determineWinner("Scissors", "Paper") == "Scissors"
    assert determineWinner("Rock", "Rock") == "Draw"
    assert determineWinner("Paper", "Paper") == "Draw"

@patch('rockPaperScissors.generateComputerMove')
def test_playRound(mock_generateComputerMove):
    mock_generateComputerMove.return_value = "Paper"
    assert playRound("Rock") == "Computer Wins!"

    mock_generateComputerMove.return_value = "Scissors"
    assert playRound("Paper") == "Computer Wins!"

    mock_generateComputerMove.return_value = "Scissors"
    assert playRound("Scissors") == "Draw"
