string = input("Enter a string: ")
letter = input("Enter a letter: ")
new_string = ""

for char in string:
    if char != letter:
        new_string = new_string + char
print(new_string)


