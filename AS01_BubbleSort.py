Myarray = [2, 4, 8, 1, 3, 9, 4]
length = len(Myarray)
Swaps = False
while 0 < 1:
    Swaps = False
    for i in range(length-1):
        if Myarray[i] > Myarray[i+1]:
            Temp = Myarray[i]
            Myarray[i] = Myarray[i+1]
            Myarray[i+1] = Temp
            Swaps = True
    if Swaps == False:
        break
    length = length - 1
print(Myarray)
