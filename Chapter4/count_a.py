string = input("Enter a sentence: ")
counter = 0

for char in string:
    if char == "a":
        counter += 1
if counter > 1:
    print("The letter ""a"" appears in your sentence", counter , "times.")
elif counter == 0:
    print("The letter ""a"" does not appear in your sentence.")
elif counter == 1:
    print("The letter ""a"" appears in your sentence", counter, "time.")

