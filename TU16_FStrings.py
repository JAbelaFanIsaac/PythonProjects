#Part 1

Ringgit = 129.000
print(f"RM{Ringgit:.2f}")

#Part 2

number = [17, 89, 25, 107]

for i in range(4):
    print(f"Binary: {number[i]:b}   Hexadecimal: {number[i]:x}  Decimal: {number[i]:d}")

#Part 3

final =""
value = int(input("Number"))
while value != 0:
    remainder = value % 2
    value = value //2
    final = str(remainder) + final
print(final)
