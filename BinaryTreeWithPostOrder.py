import random

arrayNodes = [[-1,-1,-1] for i in range(20)]

RootPointer = -1
FreeNode = 0

def AddNode(arrayNodes,rootPointer, freeNode, data):
    if freeNode <= 19:
        arrayNodes[freeNode][0] = -1
        arrayNodes[freeNode][1] = data
        arrayNodes[freeNode][2] = -1
        if rootPointer == -1:
            global RootPointer
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = rootPointer
            while Placed == False:
                if data < arrayNodes[CurrentNode][1]:
                    if arrayNodes[CurrentNode][0] == -1:
                        arrayNodes[CurrentNode][0] = freeNode
                        Placed = True
                    else:
                        CurrentNode = arrayNodes[CurrentNode][0]
                else: 
                    if arrayNodes[CurrentNode][2] == -1:
                        arrayNodes[CurrentNode][2] = freeNode
                        Placed = True
                    else:
                        CurrentNode = arrayNodes[CurrentNode][2]
        global FreeNode
        FreeNode = freeNode+1
    else:
        print("tree is full")


def PrintAll():
    print("Left Pointer, Data, Right Pointer")
    for i in range(FreeNode):
        print(arrayNodes[i])


def InOrder(Node):
    if arrayNodes[Node][0] != -1: #Checks if there is a smaller node
        InOrder(arrayNodes[Node][0])  #If so, moves that to the current node
    print(arrayNodes[Node][1]) #When left most is reached, print that node
    if arrayNodes[Node][2] != -1: #Make sure rigHt not empty
        InOrder(arrayNodes[Node][2]) #expand RigHt side


for i in range(10):
    numberX = random.randint(1, 100)
    AddNode(arrayNodes, RootPointer, FreeNode, numberX)
PrintAll()
InOrder(0)
