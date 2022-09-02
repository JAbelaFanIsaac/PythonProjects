import random

Goal = random.randint(100, 999)
finalnumbers = []

for i in range(6):
    S = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    B = random.choice([10, 25, 50, 75, 100])
    q = input("Big number [B] or small number [S]")
    while q != "B" and q != "S":
        q = input("Big number [B] or small number [S]")
        if q == "B":
            print(B)
            finalnumbers.append(B)
            break
        if q == "S":
            print(S)
            finalnumbers.append(S)
            break
    if q == "B":
        print(B)
        finalnumbers.append(B)
    if q == "S":
        print(S)
        finalnumbers.append(S)

print(finalnumbers)
print("Try to make", Goal)
