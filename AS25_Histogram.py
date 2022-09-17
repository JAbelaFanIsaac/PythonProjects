#Histogram
recorded = []
num = int(input("Number of lines"))
for _ in range(num):
    repeater = int(input("Number of stars"))
    recorded.append(repeater)

for i in range(num):
    print("*"*recorded[i], sep='')
