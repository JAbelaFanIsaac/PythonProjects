num = int(input("Number of lines"))
spacing = num - 2
centre = (" ")*spacing
print(centre, "A")
gap = 1
middle = (" ")*gap
last = ("A")*(2*num-1)

spacing = spacing - 1
centre = (" ")*spacing
print(centre, "A", "A")

for i in range(num - 3):
    spacing = spacing - 1
    centre = (" ")*spacing
    print(centre, "A", middle, "A")
    gap = gap + 2
    middle = (" ")*gap


print(last)
