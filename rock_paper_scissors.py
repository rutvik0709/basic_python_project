import random
print("\t\t\t\t\tWELCOME TO THE ROCK|PAPER|SCISSORS GAME")


user_score = 0
computer_score = 0
choices = ["rock","paper","scissors"]
while True:
    computer_choice=random.choice(choices)
    user_choice = input("Enter rock / paper / scissors or Q to exit: ").lower()
    if user_choice =="q":
        print("Thank you for playing this game.")
        quit()
    elif user_choice not in choices:
        print("Enter a valid choice.")
        continue
    
    if user_choice == "paper" and computer_choice == "rock":
        user_score+=1
        print("You won this round!")
    elif user_choice == "rock" and computer_choice == "scissors":
        user_score+=1
        print("You won this round!")
    elif user_choice == "scissors" and computer_choice == "paper":
        user_score+=1
        print("You won this round!")
    elif user_choice == computer_choice:
        print("Tie")
    else:
        computer_score+=1
        print("Computer won this round!")
    
    if computer_score ==5:
        print("\nComputer won the game.")
        print(f"Your score {user_score}. Computer score {computer_score}")
        quit()
    elif user_score ==5:
        print ("\nYou won the game.")
        print(f"Your score {user_score}. Computer score {computer_score}")
        quit()


