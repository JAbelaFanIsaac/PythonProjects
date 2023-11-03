import os

arrayTreasure = [] # This is acting as an array

class TreasureChest:
    def __init__(self, q, a, p): # has to be initialisation like this
        self.__question= q
        self.__answer = a
        self.__points = p


    def getValue(self):
        Message = self.__question + " " + self.__answer + " " + self.__points
        return Message

    def getQuestion(self):
        Message = self.__question
        return Message

    def checkAnswer(self, Answer):
        if self.__answer == Answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return int(int(self.__points)/2)
        elif attempts == 3:
            return int(int(self.__points)/3)
        elif attempts == 4:
            return int(int(self.__points)/4)
        else:
            return 0

def read_Data():
    try:
        with open("TreasureChestData.txt", "r") as file:
            for i in range(5):
                q = file.readline().strip()
                a = file.readline().strip()
                p = file.readline().strip()
                arrayTreasure.append(TreasureChest(q, a, p))

    except:
        print("Not found, searching file in ", os.getcwd())

read_Data()
print(arrayTreasure)
for i in range(5):
    print(arrayTreasure[i].getValue())

attempts = 1
Correct = False
number = int(input("Question 1 to 5"))
num = number -1
print(arrayTreasure[num].getQuestion())

while Correct == False:
    written = input("Write your answer")
    verify = arrayTreasure[num].checkAnswer(written)
    if verify == True:
        Correct = True
    else:
        attempts = attempts + 1

print(arrayTreasure[num].getPoints(attempts))
