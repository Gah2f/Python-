def add_one(n):
    if n >= 9:
        return n + 1
    total = n + 1
    print(total)

    return add_one(total)

add_one(0) 

def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)
    
print(factorial(4))
print(factorial(5)) 

import sys
import random
from enum import Enum

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

    if player == 1 and computer == 2:
        print("😒 You lose, paper beats rock")
    if player == 1 and computer == 3:
        print("🎉 You win, 🪨 rock beats ✂️ sissors")
    if player == 2 and computer == 1:
        print("🎉 You win, 📜 paper beats 🪨 rock")
    if player == 2 and computer == 3:
        print("😒 You lose, ✂️ sissors beats 📜 paper ")
    if player == 3 and computer == 1:
        print("😒 You lose, 🪨 rock beats ✂️ sissors")
    if player == 3 and computer == 2:
        print("🎉 You win, ✂️ sissors beats 📜 paper ")

    if player == computer:
        print("It's a tie, you both chose the same thing, play again👨‍🔬")
        
        
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