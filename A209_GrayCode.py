def GCode(n):
    Set = []
    NewSecond = []
    
    if n == 0:
        return [""]
    first = GCode(n-1)
    second = GCode(n-1)

    for j in range(len(second)-1, -1, -1):
        NewSecond.append(second[j])

    for i in range(len(first)):
        Set.append("0" + str(first[i]))
    for i in range(len(second)):
        Set.append("1" + str(NewSecond[i]))
    return Set

print(GCode(4))
