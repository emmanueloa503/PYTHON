#Emmanuel Owusu-AMpaw
#Tittle: Rock, Paper, Scissors game

from optparse import Option
import random
from ssl import Options

options = ("rock", "paper", "scissors") #choices for the cmputer variable

running =True 

while running:

    player = None
    computer= random.choice(options) #allows computer to randomly pick a choice in the option variable

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ") #player enters one of the choices listed in the options

    #both player and computer choices are printed
    print(f"Player: {player}") 
    print(f"Computer: {computer}")

    #deciding if it player won, lost, or tied against computer
    if player == computer:
            print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    
    #asking player if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    if not play_again== "y":
        running = False

#thanks player if they are done player
print("Thanks for playing!")   