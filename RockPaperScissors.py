import random

pick = int(input("Choose between 1.Rock 2.Siccors 3.Paper"))

t = random.randint(1, 3)

if t == pick:
    print("draw")
    
if t == 1 and pick == 2:
    print("Computer wins")
    
if t == 2 and pick == 3:
    print("Computer wins")

if t == 3 and pick == 1:
    print("Computer wins")

if t == 1 and pick == 3:
    print("You win")

if t == 2 and pick == 1:
    print("You win")

if t == 3 and pick == 2:
    print("You win")