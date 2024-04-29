SearchData = [i for i in range(63)]

SearchItem = int(input("Search for number: "))
X = 0

def BinarySearch(Low, High):
    global X
    Middle = int((Low+High)/2)
    if SearchData[Middle] == SearchItem:
        X = Middle
        return X
    else:
        if SearchData[Middle] < SearchItem:
            Low = Middle + 1
            return BinarySearch(Low, High)
        elif SearchData[Middle] > SearchItem:
            High = Middle-1
            return BinarySearch(Low, High)

print(BinarySearch(0, 63))
