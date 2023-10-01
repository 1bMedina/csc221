from random import randint

num1 = 1234

print("Ok, I have picked a number.")

guess = int(input("Guess a number: "))

while num1 != guess:
    print("incorrect")
    guess = int(input("Guess a number: "))
else:
    print("correct")

