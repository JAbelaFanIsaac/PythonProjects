def ackerman(a,b):
    if a == 0:
        return b + 1
    elif b == 0:
        return ackerman(a-1, 1)
    else:
        return ackerman(a-1, ackerman(a, b-1))

i = int(input("First number"))
j = int(input("Second number"))
print(ackerman(i, j))
