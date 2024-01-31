#Rock Paper Scissor Game in Python between computer and user

import random

while True:
    choices = ["rock","paper","scissor"]

    #Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer
    computer = random.choice(choices)
    player = None

    #User Input: Prompt the user to choose rock, paper, or scissors.
    while player not in choices: 
        player = input("rock,paper or scissor?").lower()

    #Result: Show the user's choice and the computer's choice.Display the result, whether the user wins, loses, or it's a tie.
    if player==computer:
        print("Computer:",computer)
        print("Player:",player)
        print("Tie!")

    elif player=="rock":
        if computer=="paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You Lose.Better Luck next Time!")
        if computer=="scissor":
            print("Computer:",computer)
            print("Player:",player)
            print("You Win!")

    elif player=="paper":
        if computer=="scissor":
            print("Computer:",computer)
            print("Player:",player)
            print("You Lose.Better Luck next Time!")
        if computer=="rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You Win!")

    elif player=="scissor":
        if computer=="rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You Lose.Better Luck next Time!")
        if computer=="paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You Win!")
            
    #Play Again: Ask the user if they want to play another round.
    player_choice = input("Do you want to play another round?(yes/no)").lower()
    if player_choice == "no":
        break

print("BYE!")