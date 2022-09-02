import random
mynumber = random.randint(1,100)
while True:
    x = int(input("What is the number?"))
    if x < mynumber:
        print("Go Higher")
    if x > mynumber:
        print("Go Lower")
    if x == mynumber:
        print("Bingo")
        break