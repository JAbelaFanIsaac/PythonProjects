n = 5

for i in range(1, n+1, 1):
    print(" "*(n-i+1), end=" ")

    C = 1
    for j in range(1, i+1):
        print("", C, end="")
        C = int(C * (i - j)/j)
    print("")
