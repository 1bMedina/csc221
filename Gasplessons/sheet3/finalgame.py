from random import randint

num1 = randint(1,1000)

print("Ok, I have picked a number between 1 and 1000")

guess = int(input("Guess a number between 1 and 1000: "))

while guess != num1:
    if guess > num1:
        print("That's too high")
    else:
        print("That's too low")
    guess = int(input("Guess again: "))
else:
    print("That's correct!")
