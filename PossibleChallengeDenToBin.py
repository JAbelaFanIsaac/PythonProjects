final =""
number = int(input("Number"))
while number != 0:
    remainder = number % 2
    number = number //2
    final = str(remainder) + final
print(final)
