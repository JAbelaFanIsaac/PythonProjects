num = input("Enter a number")

def SumDigits(value):
    if value == "":
        return 0
    else:
        biggest = value[0]
        rest = value[1:]
        return int(biggest) + SumDigits(rest)

print(SumDigits(num))
