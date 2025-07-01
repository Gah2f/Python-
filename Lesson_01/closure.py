def outer(x):
    def inner(y):
        return x + y
    return inner
add_five = outer(5)
print(add_five(10)) 

def parents(person, coins):
    
    def playgame():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
         print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " has no coins left.")

    return playgame
leul = parents("Leul", 6)
meba = parents("Meba", 5)
leul()  
leul()
meba()

import sys
import random
from enum import Enum

def game(): 
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_game():
        nonlocal  player_wins, computer_wins
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
            nonlocal player_wins, computer_wins
            if player == 1 and computer == 2: 
                computer_wins += 1
                return "😒 You lose, paper beats rock"
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win, 🪨 rock beats ✂️ sissors"
            if player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win, 📜 paper beats 🪨 rock"
            if player == 2 and computer == 3:
                computer_wins += 1
                return "😒 You lose, ✂️ sissors beats 📜 paper "
            if player == 3 and computer == 1:
                computer_wins += 1
                return "😒 You lose, 🪨 rock beats ✂️ sissors"
            if player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win, ✂️ sissors beats 📜 paper "

            if player == computer:
                return "It's a tie, you both chose the same thing, play again👨‍🔬"
        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\n\n You have played {game_count} games so far.")
        print(f"\n\n Player wins: {player_wins}  \n\n Computer wins: {computer_wins}")
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
    return play_game

play= game()
play()  
