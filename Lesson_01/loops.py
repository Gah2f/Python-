import random
value = 1
while value < 10: 
 
    print(value) 
    if (value == 4):
        break
    value += 1

value = 10

while value > 0:
    print(value)
    value -= 1

MYHOME= ["home", "is", "where", "the", "heart", "is"]

for word in MYHOME:
    print(word)  

for i in range(5):
    print(i)

for i in 'Nebiyu':
    print(i)

for j in 'Leul':
    print("\n",j)

for word in MYHOME:
    if (word == "the"):
        break
    print(word)

for word in MYHOME:
    if (word == "the"):
        continue
    print(word)

name = ["Nebiyu", "Leul ", "Meba"]
works = ["Coding", "Eating", "playing"]
for i in name:
    for j in works:
        print(i ," ","is", " ", j) 

import sys
import random
from enum import Enum

class Choices(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True
while playagain: 
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
        sys.exit("Invalid choice, please choose 1, 2, or 3.")


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

    playagain = input("\n\n Do you want to play again? (yes/no) Y for yes and N for NO:\n\n ")
    if playagain.lower() == 'y':
     continue
    else:
     print("Thanks for playing! Goodbye! 👋")
    playagain = False