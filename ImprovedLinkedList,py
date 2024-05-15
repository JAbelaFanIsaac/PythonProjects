#LinkedList

Data = [0 for i in range(10)]
Pointer = [-1 for i in range(10)]

FrontPointer = None
HeapPointer = None

def StartList(data):
    global FrontPointer
    global HeapPointer

    FrontPointer = 0

    Data[FrontPointer] = data
    HeapPointer = 1

def AddNode(data):
    global FrontPointer
    global HeapPointer

    Data[HeapPointer] = data
    Pointer[FrontPointer] = HeapPointer
    HeapPointer = HeapPointer + 1
    FrontPointer = FrontPointer + 1

def RemoveNode(data):
    #search for target node, bridge gaps if necessary
    target = -1
    bridging = -1
    for i in range(len(Data)):
        if Data[i] == data:
            target = i

    Pointing = Pointer[target]

    for i in range(len(Data)):
        if Pointer[i] == target:
            bridging = i

    Pointer[bridging] = Pointing
    Data[target] = 0
    Pointer[target] = -1

StartList(3)
AddNode(7)
AddNode(2)
RemoveNode(7)
AddNode(5)
AddNode(6)
AddNode(9)

print(Data)
print(Pointer)
