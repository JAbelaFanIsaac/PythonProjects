Data = [1, 9, 7, 3, 11, 10, 5, 2, 6]

def enqueue(value):
    Data.append(value)

def dequeue():
    if len(Data) == 0:
        print("No elements in stack")
    else:
        print(Data[0])
        Data.remove(Data[0])
