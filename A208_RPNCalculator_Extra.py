import math
arrayNum = []
arrayTemp = []

def pop():
    global arrayTemp
    length = len(arrayTemp)-1
#    print("length:", length)
    temp = str(arrayTemp[length])
    del arrayTemp[length]
    return temp

def push(value):
    arrayTemp.append(str(value))

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
    if (val == "+" or val == "-" or val == "/" or val == "*"):
        return 1
    if val == "sin" or val == "cos" or val == "tan":
        return 2
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
#        print(placeholder)
        if placeholder == "pi":
            arrayTemp.append(math.pi)
        else:
            try:
                if int(placeholder) == int(placeholder):
                    arrayTemp.append(arrayNum[i])
            except:
#                print(len(arrayTemp))
                if len(arrayTemp) == 0:
                    print("Error")
                    break
#                print("operator:", isOperator(sequence[i]))
                if isOperator(sequence[i]) == 1:
                    num2 = pop()
                    num1 = pop()
                    newVal = 0
                    if sequence[i] == "+":
                        newVal = float(num1) + float(num2)
                    if sequence[i] == "-":
                        newVal = float(num1) - float(num2)
                    if sequence[i] == "/":
                        newVal = float(num1) / float(num2)
                    if sequence[i] == "*":
                        newVal = float(num1) * float(num2)
                    push(newVal)

                if isOperator(sequence[i]) == 2:
                    number = pop()
                    Value1 = 0
                    if sequence[i] == "sin":
                        Value1 = math.sin(float(number))
                    if sequence[i] == "cos":
                        Value1 = math.cos(float(number))
                    if sequence[i] == "tan":
                        Value1 = math.tan(float(number))
                    push(Value1)
else:
    print("Nothing Happens")
print(arrayTemp)
