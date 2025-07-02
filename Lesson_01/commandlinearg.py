# def hello(name,lang):
#     greetings = {
#         "en": "Hello",
#         "es": "Hola",
#         "fr": "Bonjour",
#     }
#     msg = f"{greetings[lang]}, {name}!"
#     print(msg)

# if __name__ == "__main__":

#     import argparse


#     parser = argparse.ArgumentParser(
#         description="A simple command line argument parser example."
#     ) 

#     parser.add_argument(
#         "-n", "--name", metavar="name", required=True,
#         help="The name to greet."
#     ) 
#     parser.add_argument(
#         "-l", "--lang", metavar="language",  required=True, choices=["en", "es", "fr"], help="The language for the greeting (en, es, fr)."
#     )
#     args = parser.parse_args()

#     hello(args.name, args.lang) 

import sys
import random
from enum import Enum

def game(name= "Player one"): 
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_game():
        nonlocal name
        nonlocal  player_wins, computer_wins
        class Choices(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("Welcome to the Rock, Paper, Scissors game! \n\n")
        print("")


        playerChoice = input(f" {name} , Enter your choice ... \n 1 for 🪨   rock \n 2 for 📜   paper \n 3 for ✂️   sissors: \n  \n")
        player = int(playerChoice)
    
        if playerChoice not in ["1", "2", "3"]:
            sys.exit(f" {name} , Invalid choice, please choose 1, 2, or 3.")
            return play_game()
        if player == 1:
            print(f"{name}, you chose rock")
        if player == 2:
            print(f"{name}, you chose paper")
        if player == 3:
            print(f"{name}, you chose scissors")


        computerChoice = random.choice("123")
        computer = int(computerChoice)

        print ( "Computer choose", computerChoice)
        print(f"So {name} choose {str(Choices(player)).replace('Choices.', ' ')} and computer choose {str(Choices(computer)).replace('Choices.', ' ')}")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins, computer_wins
            if player == 1 and computer == 2: 
                computer_wins += 1
                return f"😒 {name}, you lose, paper beats rock"
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win, 🪨 rock beats ✂️ sissors"
            if player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win, 📜 paper beats 🪨 rock"
            if player == 2 and computer == 3:
                computer_wins += 1
                return f"😒 {name}, you lose, ✂️ sissors beats 📜 paper "
            if player == 3 and computer == 1:
                computer_wins += 1
                return f"😒 {name}, you lose, 🪨 rock beats ✂️ sissors"
            if player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win, ✂️ sissors beats 📜 paper "

            if player == computer:
                return f"It's a tie, {name} and computer chose the same thing, play again👨‍🔬"
        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\n\n {name}, you have played {game_count} games so far.")
        print(f"\n\n Player wins: {player_wins}  \n\n Computer wins: {computer_wins}")
        print(f"\n {name}, Do you want to play again?")
        while True:
            playagain = input(f"\n\n {name}, (yes/no) Y for yes and N for NO:\n\n ")
            if playagain.lower() not in ['y', 'n']:
                print("Invalid input, please enter 'y' or 'n'.")
                continue
            if playagain.lower() == 'y':
                return play_game()
            else:
                print(f"Thanks for playing! {name}, Goodbye! 👋")
                sys.exit("Goodbye! 👋")
    return play_game


if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    ) 

    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="The name of the player.") 
  
    args = parser.parse_args()
 
    play= game(args.name) 
    play()  
