import random
print("\t\t\t\t\t!!GUESS THE NUMBER!!")

range = input("Enter the range: ")

if range.isdigit():
    range = int(range)

    if range<0:
        print("Range cannot be.")
        quit()

else :
    print("Enter a valid number.")
    quit()



guess_number = random.randint(0, range)


guess =0
while True:
    user_guess =input("\nGuess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess<0:
            print("Enter number greater than 0.")
            quit()

    else:
        print("Enter a valid number.")
        quit()

    if user_guess > guess_number:
        print("Enter a lower number.\n")
        guess+=1
    elif user_guess < guess_number:
        print("Enter a larger number.\n")
        guess+=1
    elif user_guess == guess_number:
        guess+=1
        break
print(f"\nThe number you were guessing was {guess_number} and you took {guess} attempts.")
