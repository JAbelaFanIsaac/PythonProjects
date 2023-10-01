MyArray = [12, 4, 64, 32, 1, 5, 87, 35, 49, 14, 45, 103, 24, 167, 91]

def insertionSort(numseq):
    boundary = len(numseq)
    for i in range(1, boundary):
        temp = numseq[i]
        pointer = i-1
        while pointer > -1 and temp < numseq[pointer]:
            numseq[pointer+1] = numseq[pointer]
            pointer = pointer - 1
        numseq[pointer+1] = temp
    print(numseq)

insertionSort(MyArray)
