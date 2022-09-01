import random
options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
y = random.choice(options)
name = input("What is your name?")
print(y)
points = 0
while 0 < 1:
    if y == "1":
        print("What type of validation is range check?")
        print("1 Check data is in a certain range")
        print("2 Check if word is in a dictionary")
        print("3 Check data has the correct number of characters")
        Q1 = int(input(""))
        if Q1 == 1:
            points = points + 1
        options.remove("1")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "2":
        print("What type of validation is character check?")
        print("1 Check data is in a certain range")
        print("2 Check if word is in a dictionary")
        print("3 Check data type is expected")
        Q1 = int(input(""))
        if Q1 == 3:
            points = points + 1
        options.remove("2")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "3":
        print("What type of validation is check digit?")
        print("1 Check data has correct last numbers")
        print("2 Check if word is a certain length")
        print("3 Check data has the correct number of characters")
        Q1 = int(input(""))
        if Q1 == 1:
            points = points + 1
        options.remove("3")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "4":
        print("What type of validation is presence check?")
        print("1 Check data is in a certain range")
        print("2 Check if word is in a dictionary")
        print("3 Check that there is at least a character")
        Q1 = int(input(""))
        if Q1 == 3:
            points = points + 1
        options.remove("4")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "5":
        print("What type of validation is length check?")
        print("1 Check word is in a table")
        print("2 Check if data is a certain length")
        print("3 Check data has the correct number of letters")
        Q1 = int(input(""))
        if Q1 == 2:
            points = points + 1
        options.remove("5")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "6":
        print("What type of validation is lookup check?")
        print("1 Check data is in a certain range")
        print("2 Check if word is in a dictionary")
        print("3 Check data is in a table")
        Q1 = int(input(""))
        if Q1 == 3:
            points = points + 1
        options.remove("6")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "7":
        print("What type of validation is format check?")
        print("1 Check data is a certain type")
        print("2 Check if word has a consistant font")
        print("3 Check data is in the same language")
        Q1 = int(input(""))
        if Q1 == 1:
            points = points + 1
        options.remove("7")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "8":
        print("What type of verification is double entry?")
        print("1 Check if data is repeatable")
        print("2 Check if word is acceptable in a table")
        print("3 Check data has too many digits")
        Q1 = int(input(""))
        if Q1 == 1:
            points = points + 1
        options.remove("8")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "9":
        print("What type of verification is visual check?")
        print("1 Check if word is present")
        print("2 Check if word is in a dictionary")
        print("3 Check data is exactly the same as preset data")
        Q1 = int(input(""))
        if Q1 == 3:
            points = points + 1
        options.remove("9")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "10":
        print("What type of verification is parity check?")
        print("1 Check data via end digit")
        print("2 Check data is present")
        print("3 Check data is exactly similar to answer")
        Q1 = int(input(""))
        if Q1 == 1:
            points = points + 1
        options.remove("10")
        if len(options) == 0:
            break
        y = random.choice(options)
    if y == "11":
        print("What type of verification is checksum?")
        print("1 Check data is valid by addition")
        print("2 Check if number is valid through calculations")
        print("3 Check data has the correct number of characters")
        Q1 = int(input(""))
        if Q1 == 2:
            points = points + 1
        options.remove("11")
        if len(options) == 0:
            break
        y = random.choice(options)
print("Game over")
print(name, "You got", points, "points")