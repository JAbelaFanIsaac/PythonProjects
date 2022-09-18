x = int(input("How old are you?"))
y = int(input("What is you heart rate?"))
z = 0.7*(225-x)
if y < z:
    print("Your okay")
elif y == z:
    print("Your at your maximum heart rate")
elif y > z:
    print("You need to slow down your heart rate")