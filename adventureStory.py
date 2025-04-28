# Matthew Petersen          02-17-2025
# Use the Python programming language to write a short interactive 'story' using if statements to control the flow of the narrative,
# and the input() function to let the user decide what to do next

def main():
    print("Welcome to the adventure through Iowa State Universuty!")

    
    print("You find yourself standing next to the clocktower of Iowa State.")
    choice1 = input("Would you rather go [left] to go get food at windows, or [right] towards beardshear, or [forward] into the Memorial Union?: ").lower()
    
    if choice1 == "left":
        print("\nYou enter windows and is introduced to a funky smell and two seperate lines for two different meals.")
        choice2 = input("Do you want to [go right] and have mac and cheese or [go left] and have some deliciouse Orange chicken?: ").lower()
        
        if choice2 == "go right":
            print("\nYou end up chosing mac and cheese which is very fulling and comes with pulled pork and corn but you end up getting food poisoning.")
        if choice2 == "go left":
            print("You end up having a delicious orange chicken that is tangy and will fill you up instantly and you meet a new friend in line. ")

    elif choice1 == "right":
        print("\nYou walk towards beardshear which has amazing architectual designs and is one of the biggest buildings at Iowa State.")
        choice2 = input("Do you want to [enter] the building or [pass] around the building and not go in?: ").lower()
        
        if choice2 == "enter":
            print("\nYou entered Beardshear where you are introduced to a great interior. You end up running into one of your friends from back home that you havent seen for a while and end up having a great conversation!")
            
        if choice2 == "pass":
            print("You have passed the building and end up tripping on a curb and end up losing a tooth. Maybe you should have gone into Beardshear.")
       

    elif choice1 == "forward":
        print("\nYou step into the Memorial Union where there are many students roaming.")
        choice2 = input("Do you want to go to the [store] where you will find many Iowa State merchandise, or [eat] at one of the many food options?: ").lower()
        
        if choice2 == "store":
            print("\nYou end up going to the store and finding a T-shirt you really like.")
            choice3 = input("Do you [buy] the shirt or [decline] the temptation?: ").lower()
            
            if choice3 == "buy":
                print("\nTYour mother loves you and buys it for you!")

            if choice3 == "decline":
                print("You will never find that shirt ever again and you will always be thinkingh I should have bought that shirt.")
        
            else:
                print("You end up buying the shirt yourself and realize that you will never wear it right after you bought it.")

        else:
            print("\nInstead of doing either you hide yourself from the other students and pretend like your not there.")

    else:
        print("\nYou tell your parents you want to go back home and you dont end up attending Iowa State.")
        print("Your adventure through the school ends and youregret the decision of not going to Iowa State becuase WE ARE SO COOL.")

if __name__ == "__main__":
    main()
