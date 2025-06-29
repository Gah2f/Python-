name = "Nebiyu" # This is a global variable

def greet():
    print("Hello, " + name + "!")

greet() 

def local_scope():
    name = "Local Nebiyu"  # This is a local variable
    print("Hello, " + name + "!")

local_scope() 

def enclosing_scope():
    name = "Enclosing Nebiyu"  # This is a Enclosing variable
    def inner_function():
        print("Hello, " + name + "!")
    inner_function()

enclosing_scope()

import sys
import random
from enum import Enum

game_count = 0

def play_game():

    class Choices(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print("Welcome to the Rock, Paper, Scissors game! \n\n")
    print("")


    playerChoice = input("Enter your choice ... \n 1 for 🪨   rock \n 2 for 📜   paper \n 3 for ✂️   sissors: \n  \n")
    player = int(playerChoice)
  
    if playerChoice not in ["1", "2", "3"]:
        sys.exit("Invalid choice, please choose 1, 2, or 3.")
        return play_game()
    if player == 1:
        print("You chose rock")
    if player == 2:
        print("You chose paper")
    if player == 3:
        print("You chose scissors")
   

    computerChoice = random.choice("123")
    computer = int(computerChoice)

    print ( "Computer choose", computerChoice)
    print("So you choose", str(Choices(player)).replace("Choices.", " ") ," ","and", " ", "computer choose", str(Choices(computer)).replace("Choices.", " "))
 
    def decide_winner(player, computer):
        if player == 1 and computer == 2:
            return "😒 You lose, paper beats rock"
        if player == 1 and computer == 3:
            return "🎉 You win, 🪨 rock beats ✂️ sissors"
        if player == 2 and computer == 1:
            return "🎉 You win, 📜 paper beats 🪨 rock"
        if player == 2 and computer == 3:
            return "😒 You lose, ✂️ sissors beats 📜 paper "
        if player == 3 and computer == 1:
            return "😒 You lose, 🪨 rock beats ✂️ sissors"
        if player == 3 and computer == 2:
            return "🎉 You win, ✂️ sissors beats 📜 paper "

        if player == computer:
            return "It's a tie, you both chose the same thing, play again👨‍🔬"
    game_result = decide_winner(player, computer)
    print(game_result)
    global game_count
    game_count += 1
    print(f"\n\n You have played {game_count} games so far.")
    print("\n Do you want to play again?")
    while True:
        playagain = input("\n\n (yes/no) Y for yes and N for NO:\n\n ")
        if playagain.lower() not in ['y', 'n']:
            print("Invalid input, please enter 'y' or 'n'.")
            continue
        if playagain.lower() == 'y':
            return play_game()
        else:
            print("Thanks for playing! Goodbye! 👋")
            sys.exit("Goodbye! 👋")

play_game()