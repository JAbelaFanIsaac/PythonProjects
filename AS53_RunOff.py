DataBlocks = []
with open("ElectionData.txt", "r") as file:
    for line in file:
        chunk = []
        first, second, third = line.split(", ")
        third = third.strip()
        chunk.append(first)
        chunk.append(second)
        chunk.append(third)
        DataBlocks.append(chunk)

print(DataBlocks)

def NewList(Name):
    NewList = []
    for i in range(len(DataBlocks)):
        NewChunk = []
        for j in range(3):
            if DataBlocks[i][j] != Name:
                NewChunk.append(DataBlocks[i][j])
        NewList.append(NewChunk)
    print(NewList)
    WinCondition(NewList)


def Count(value):
    a = 0
    b = 0
    c = 0
    breaking = False
    full = len(value)
    for i in range(full):
        if value[i] == "Alice":
            a = a + 1
        if value[i] == "Bob":
            b = b + 1
        if value[i] == "Charlie":
            c = c + 1
    if a >= int(full/2) + 1 :
        print("Alice Wins")
        breaking = True
    if b >= int(full/2) + 1 :
        print("Bob Wins")
        breaking = True
    if c >= int(full/2) + 1 :
        print("Charlie Wins")
        breaking = True
    if breaking == False:
        print("RunOff")
        if a < b and a < c:
            print("a")
            NewList("Alice")
        elif b < c:
            print("b")
            NewList("Bob")
        else:
            print("c")
            NewList("Charlie")

def WinCondition(data):
    Winner = []
    for i in range(len(data)):
        Winner.append(data[i][0])
    Count(Winner)

WinCondition(DataBlocks)
