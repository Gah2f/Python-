# a = "******************"
# b= "*     Wellcome    *"
# c= "*                 *" 

# print("" + a + "\n" + b + "\n" + c + "\n" + c + "\n" + a)

# a = 10
 
# if a > 5:
#     print("a is greater than 5")
# else: 
#     print("a is not greater than 5") 
     
     
# print("a is greaterthan 5") if a > 5 else print("a is not greater than 5")

name = "Enter your name"
print(type(name))

multiline_string = """This is a multiline string."""

# value = input("Enter a value: ")

# print("You entered:", value)

import sys
import random
from enum import Enum

class Choices(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3



print("Welcome to the Rock, Paper, Scissors game! \n\n")
print("")


playerChoice = input("Enter your choice ... \n 1 for 🪨   rock \n 2 for 📜   paper \n 3 for ✂️   sissors: \n  \n")
player = int(playerChoice)

if player == 1:
    print("You chose rock")
if player == 2:
    print("You chose paper")
if player == 3:
    print("You chose scissors")
if player != 1 and player != 2 and player != 3: 
    sys.exist("Invalid choice, please choose 1, 2, or 3.")


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
