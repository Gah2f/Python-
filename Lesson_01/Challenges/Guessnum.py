from os import name
import random
def guessnum(name="Player one"):
    game_count = 0
    def play():
        nonlocal name
        print(f"Welcome to the Guess the Number game, {name}! 🎮")
        your_number =  input("\n Guess a number from 1, 2 and 3 \n\n\n ")
        computer_number = random.choice(["1", "2", "3"])
        print(f" {name} Your choice is: {your_number}")

        computer = int(computer_number)
        def check_input(your_number): 
            if your_number == computer:
                print(f"Congratulations!, {name}🎉 You guessed the right number.")
            else:
                print(f"Sorry😒, the correct number was {computer}.")
        nonlocal game_count
        game_count += 1
        print(f"You have played {game_count} games.")
        print("Would you like to play again? (yes/no) Y for yes, N for no")
        while True:
         if input().lower() == 'y':
            return guessnum()
         else: 
            print("Thanks for playing!👋")
    return play
if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    ) 

    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="The name of the player.") 
  
    args = parser.parse_args()

    start = guessnum(args.name)
    start()