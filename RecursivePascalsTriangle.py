n = 5
count = 1

def recursivePascals(count):
    global n
    Breaker = False
    if n == count:
        Breaker = True

    for i in range(1, count + 1, 1):
        print(" " * (count - i + 1), end=" ")

        C = 1
        for j in range(1, i + 1):
            print("", C, end="")
            C = int(C * (i - j) / j)
        print("")

    count = count+1

    if Breaker == True:
        return ""

    return recursivePascals(count)

print(recursivePascals(count))
