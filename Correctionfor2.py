"""
MyArray = [12, 4, 64, 32, 1, 5, 87, 35, 49, 14, 45, 103, 24, 167, 91]

def insertionSort(digitList):
    boundary = len(digitList) #length of array
    for i in range(1, boundary):
        temp = digitList[i] #temp value
        pointer = i-1 #check value below temp
        while pointer > -1 and temp < digitList[pointer]: #make sure not at first term and not in order
            digitList[pointer+1] = digitList[pointer] #position slot gets replaced
            pointer = pointer - 1 #look at the next pair set up
        digitList[pointer+1] = temp #final insertion
    print(digitList)

insertionSort(MyArray)

"""
def insert_sort_number(number):
    valueEnd = 0
    totalNum = ""
    digitList = []
    stringed = str(number)
    for i in range(len(stringed)):
        digit = int(stringed[i])
        digitList.append(digit)

    print(digitList)
    print(digitList[0])
    #Sorting

    boundary = len(digitList) #length of array
    for i in range(1, boundary):
        temp = digitList[i] #temp value
        pointer = i-1 #check value below temp
        while pointer > -1 and temp < digitList[pointer]: #make sure not at first term and not in order
            digitList[pointer+1] = digitList[pointer] #position slot gets replaced
            pointer = pointer - 1 #look at the next pair set up
            digitList[pointer+1] = temp #final insertion
    print(digitList)

    for i in range(5):
        dig = digitList[i]
        totalNum = str(totalNum) + str(dig)
    valueEnd = int(totalNum)

    return valueEnd

print(insert_sort_number(52348))

