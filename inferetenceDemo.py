# Matthew Petersen 
# 4-21-2025
# Lab Week 14
# 
#
# Descriptions: This code creates a game in which you are able to chose what character you want to be. 
# You can be a cat, Dragon, Werewolf, and Tiger, After that you can type out whatever you want your name to be.
# Then you will battle a randomly generated opponent and will result in a winner and a loser.  
#   


import random

class Animal:
    def __init__(self, name, age, color, cost):
        self.name = name
        self.age = age
        self.color = color
        self.cost = cost

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Color: {self.color}, Cost: ${self.cost}")

    def speak(self):
        return "Hello"

    def attack_power(self):
        return self.age 


class Cat(Animal):
    def speak(self):
        return "Meow!" * self.age


class Dragon(Animal):
    def speak(self):
        return "Hiss" + ("." * self.age)


class Werewolf(Animal):
    def speak(self):
        return "G" + ("r" * self.age)


class Robot:
    def __init__(self, power):
        self.power = power

    def beep(self):
        return "beep " * self.power

    def get_power_level(self):
        return self.power


class Tiger(Cat, Robot):
    def __init__(self, name, age, color, cost, strength, power):
        Cat.__init__(self, name, age, color, cost)
        Robot.__init__(self, power)
        self.strength = strength

    def __str__(self):
        return super().__str__() + f", Strength: {self.strength}"

    def yell(self):
        return ("Roar" + "!" * self.strength) * self.age

    def attack_power(self):
        return self.strength * self.age + self.get_power_level()


def choose_character():
    print("\nChoose your character:")
    print("1. Cat")
    print("2. Dragon")
    print("3. Werewolf")
    print("4. Tiger")
    choice = input("Enter number: ")
    name = input("Enter your character's name: ")
    age = random.randint(1, 10)
    color = random.choice(["Red", "Blue", "Black", "Orange"])
    cost = random.randint(100, 1000)

    if choice == "1":
        return Cat(name, age, color, cost)
    elif choice == "2":
        return Dragon(name, age, color, cost)
    elif choice == "3":
        return Werewolf(name, age, color, cost)
    elif choice == "4":
        strength = random.randint(1, 5)
        power = random.randint(1, 5)
        return Tiger(name, age, color, cost, strength, power)
    else:
        print("Invalid choice. Defaulting to Cat.")
        return Cat(name, age, color, cost)


def random_enemy():
    enemies = [
        Dragon("Smaug", 6, "Green", 600),
        Werewolf("Fenrir", 5, "Black", 550),
        Cat("Clawdia", 4, "White", 300),
        Tiger("Stripe", 5, "Orange", 400, 3, 2)
    ]
    return random.choice(enemies)


def battle(player, enemy):
    print("\n⚔️ Battle Start!")
    print(f"You: {player}")
    print(f"Enemy: {enemy}")

    print(f"\n{player.name} says: {player.speak()}")
    print(f"{enemy.name} says: {enemy.speak()}")

    player_power = player.attack_power()
    enemy_power = enemy.attack_power()

    print(f"\n{player.name}'s Attack Power: {player_power}")
    print(f"{enemy.name}'s Attack Power: {enemy_power}")

    if player_power > enemy_power:
        print(f"\n🎉 {player.name} wins the battle!")
    elif player_power < enemy_power:
        print(f"\n💀 {enemy.name} defeats you...")
    else:
        print("\n🤝 It's a tie!")


def main():
    print("🐾 Welcome to the Animal Arena Game!")
    player = choose_character()
    enemy = random_enemy()
    battle(player, enemy)


if __name__ == "__main__":
    main()


    

