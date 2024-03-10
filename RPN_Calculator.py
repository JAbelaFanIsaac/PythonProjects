arrayNum = []
arrayTemp = []

def pop():
    global arrayTemp
    length = len(arrayTemp)-1
    temp = str(arrayTemp[length])
    del arrayTemp[length]
    return temp

def push(value):
    arrayTemp.append(int(value))

sequence = input("Write in a RPN sequence (seperate by commas): ").split(",")
valid = True

#finding how many terms there are
try:
    edging = 0
    while 0 < 1:
        if sequence[edging]:
            edging = edging + 1
except:
    print(edging)

def isOperator(val):
    if val == "+" or val == "-" or val == "/" or val == "*":
        return True
    else:
        global valid
        valid = False
        return -1

if edging == 0:
    valid = False

if valid == True:
    for i in range(edging):
        arrayNum.append(str(sequence[i]))

    print(arrayNum)
    #checking remaining
    for i in range(edging):
        placeholder = arrayNum[i]
        try:
            if int(placeholder) == int(placeholder):
                arrayTemp.append(arrayNum[i])
        except:
            print(len(arrayTemp))
            if len(arrayTemp) <= 1:
                print("Error")
                break
            num2 = pop()
            num1 = pop()
            if sequence[i] == "+":
                newVal = int(num1) + int(num2)
            if sequence[i] == "-":
                newVal = int(num1) - int(num2)
            if sequence[i] == "/":
                newVal = int(num1) / int(num2)
            if sequence[i] == "*":
                newVal = int(num1) * int(num2)
            push(int(newVal))
else:
    print("Nothing Happens")
print(arrayTemp)
