# Ultimate TODO list 
# Matthew Petersen
# 04-16-2025
# Assignment #5 
# 
# 
# DESCRIPTIONS: This code will allow us to generate a TODO list which helps us put sertain objectives into a backlog
# in which we are able to move them around into different subjects. We are able to delete these items and save
# the lost you are computing. 

import sys
import pickle

def printTitleMaterial():
    print("The Ultimate TODO List!")
    print()
    print("By: Matthew Petersen")
    print("[COMS 1270]")
    print()

def initList():
    todoList = {
        "backlog": [],
        "todo": [],
        "in_progress": [],
        "in_review": [],
        "done": []
    }
    return todoList

def checkIfListEmpty(todoList):
    return all(len(todoList[key]) == 0 for key in todoList)

def saveList(todoList):
    listName = input("Enter List Name (Exclude .lst Extension): ")
    try:
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
        print(f"List saved to ./{listName}.lst")
    except:
        print(f"ERROR (saveList): ./{listName}.lst is not a valid filename!")
        sys.exit()

def loadList():
    listName = input("Enter List Name (Exclude .lst Extension): ")
    try:
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
        print(f"List loaded from ./{listName}.lst")
        return todoList
    except:
        print(f"ERROR (loadList): ./{listName}.lst was not found!")
        sys.exit()

def checkItem(item, todoList):
    for key in todoList:
        if item in todoList[key]:
            return True, key, todoList[key].index(item)
    return False, "", -1

def addItem(item, toList, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if not itemFound:
        todoList[toList].append(item)
    else:
        print("ERROR: '{0}' already exists in the '{1}' list at index {2}.".format(item, keyName, index))
    return todoList

def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound:
        del todoList[keyName][index]
    else:
        print("ERROR: Cannot delete '{0}' because it does not exist.".format(item))
    return itemFound, todoList

def moveItem(item, toList, todoList):
    itemFound, todoList = deleteItem(item, todoList)
    if itemFound:
        todoList = addItem(item, toList, todoList)
    else:
        print("ERROR: Cannot move '{0}' because it does not exist.".format(item))
    return todoList

def printTODOList(todoList):
    for key in todoList:
        print(f"{key}: {todoList[key]}")
    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ").strip().lower()

        if choice == "a":
            item = input("Enter the item to add to the backlog: ")
            addItem(item, "backlog", todoList)
            printTODOList(todoList)

        elif choice == "m":
            if checkIfListEmpty(todoList):
                print("No items to move!")
            else:
                item = input("Enter the item to move: ")
                found, _, _ = checkItem(item, todoList)
                while not found:
                    print(f"Error: '{item}' does not exist in the todo list.")
                    item = input("Enter a valid item to move: ")
                    found, _, _ = checkItem(item, todoList)

                target_key = input("Enter the category (key) to move the item to: ")
                while target_key not in todoList:
                    print(f"Error: '{target_key}' is not a valid category.")
                    target_key = input("Enter a valid category key to move the item to: ")

                moveItem(item, target_key, todoList)
                printTODOList(todoList)

        elif choice == "d":
            if checkIfListEmpty(todoList):
                print("No items to delete!")
            else:
                item = input("Enter the item to delete: ")
                success, todoList = deleteItem(item, todoList)
                if success:
                    print(f"'{item}' has been deleted.")
                printTODOList(todoList)

        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)

        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()
    return todoList

def main():
    taskOver = False
    printTitleMaterial()

    while not taskOver:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ").strip().lower()
        print()

        if choice == "n":
            todoList = initList()
            printTODOList(todoList)
            runApplication(todoList)

        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)

        elif choice == "q":
            taskOver = True
            print("Goodbye!\n")

        else:
            print("Please enter [n], [l], or [q]...\n")

if __name__ == "__main__":
    main()
