from random import randint

num1 = randint(1, 1000)

print("Ok, I have picked a number 1 through 1000.")

guess = input("Guess a number between 1 and 1000: ")

if guess == num1:
    print("correct!")
else:
    print("incorrect!")

