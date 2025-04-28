# Matthew Petersen
# Date Started: 03-05-2025
# Assignment number 3
#
# NIMGRAD
# We will use code to create a game between two different players. They will take turns
# removing an amount from the total with the goal os not taking the last one. 

def display_menu():
    print("\n=== NIMGRAB MENU ===")
    print("1. Play Game")
    print("2. Read Rules")
    print("3. Quit")

def display_rules():
    print("\n=== RULES OF NIMGRAB ===")
    print("- Players take turns removing items from a row.")
    print("- You must take between X and Y items per turn.")
    print("- The player who takes the last item loses the game.")

def get_valid_input(prompt, valid_choices):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def play_game(mode):
    import random
    items = random.randint(20, 25)
    X, Y = 1, 3  
    turn = 0  
    
    print(f"Starting game with {items} items!")
    while items > 0:
        print(f"\nItems remaining: {items}")
        if mode == 2 or turn == 0:
            take = get_valid_input(f"Player {turn + 1}, how many do you take ({X}-{Y})? ", range(X, min(Y, items) + 1))
        else:
            take = min(max(X, items - 1), Y)  
            print(f"Computer takes {take} items.")
        
        items -= take
        if items == 0:
            print(f"Player {turn + 1} loses!")
            break
        turn = 1 - turn 

def main():
    while True:
        display_menu()
        choice = get_valid_input("Select an option: ", [1, 2, 3])
        if choice == 1:
            mode = get_valid_input("1-player (vs AI) or 2-player? (Enter 1 or 2): ", [1, 2])
            play_game(mode)
        elif choice == 2:
            display_rules()
        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()