

import random

print("Welcome to the game of rock paper scissors!")
choices = ["rock", "paper", "scissors"]
rounds_played = 0
user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose rock paper or scissors(or type 'quit' to exit): ")
    if user_choice.lower() == "quit":
        print("Exiting the game...")
        print(f"final score - You: {user_score} | computer: {computer_score}")
        break
    
    if user_choice not in choices:
        print("Invalid game entry!")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}") 

    if user_choice == computer_choice:
        print("Its a Tie!")
    elif user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper" or user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        user_score += 1
    else:
        print("Computer won!")
        computer_score += 1

    print(f"Round score - You: {user_score} | Computer: {computer_score}")
    print("-" * 130)

    
