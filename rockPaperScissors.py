# Matthew Petersen
#  4-7-2025
# Lab Week 12
# 
# Description : This code allows us to play rock paper scissors against the computer that
# is randomly generating its response.

import random

def generateComputerMove():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determineWinner(human_move, computer_move):
    if human_move == computer_move:
        return "Draw"
    
    if (human_move == "Rock" and computer_move == "Scissors") or \
       (human_move == "Paper" and computer_move == "Rock") or \
       (human_move == "Scissors" and computer_move == "Paper"):
        return human_move
    else:
        return computer_move

def playRound(human_move):
    computer_move = generateComputerMove()
    winner_move = determineWinner(human_move, computer_move)
    
    if winner_move == "Draw":
        return "Draw"
    elif winner_move == human_move:
        return "Human Wins!"
    else:
        return "Computer Wins!"

def main():
    rounds = int(input("Enter the number of rounds to play (odd number): "))
    if rounds % 2 == 0:
        print("Please enter an odd number of rounds.")
        return

    human_score = 0
    computer_score = 0

    while human_score <= rounds // 2 and computer_score <= rounds // 2:
        human_move = input("Enter your move (Rock, Paper, Scissors): ").strip().capitalize()
        if human_move not in ["Rock", "Paper", "Scissors"]:
            print("Invalid move. Try again.")
            continue

        result = playRound(human_move)
        print(result)

        if "Human" in result:
            human_score += 1
        elif "Computer" in result:
            computer_score += 1

        if human_score > rounds // 2 or computer_score > rounds // 2:
            break

    if human_score > computer_score:
        print("You win the game!")
    elif computer_score > human_score:
        print("Computer wins the game!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()