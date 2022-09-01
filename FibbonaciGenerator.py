a = int(input("What nth term?"))

longcode = ((1 + 5**0.5)**a - (1 - 5**0.5)**a)/(2**a * 5**0.5)

fewq = longcode % 128

ert = round(fewq, 0)

print(ert)