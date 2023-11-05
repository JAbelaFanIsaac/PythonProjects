import os

arrayCats = []

class Cats():
    def __init__(self, name, des, weight, length, life, image):
        self.__name = name
        self.__description = des
        self.__weight = weight
        self.__length = length
        self.__life = life
        self.__imageURL = image

    def GetCatDetails(self):
        message = self.__name + "\n" + self.__description + "\n"+ str(self.__weight) + "\n" +\
                  str(self.__length) + "\n" + str(self.__life) + "\n" +self.__imageURL
        return message

    def GetCatLife(self):
        message = str(self.__life) + " years " + self.__name
        return message

def Constructor():
    try:
        with open("CutestCats.txt", "r") as file1:
            with open("CatsSorted.txt", "w") as file2:
                for i in range(61):
                    row = file1.readline()
                    if row != "\n":
                        file2.write(row)
        with open("CatsSorted.txt", "r") as file3:
            for j in range(5):
                name = file3.readline().strip()
                des1 = file3.readline().strip()
                weightRAW = file3.readline().strip()
                lengthRAW = file3.readline().strip()
                des2 = file3.readline().strip()
                lifeRAW = file3.readline().strip()
                image = file3.readline().strip()

                weightParts = weightRAW.split(" ")
                if weightParts[1] == "Up":
                    weight = "16.25"
                else:
                    weight = (int(weightParts[1]) + int(weightParts[3]) )/2

                lengthParts = lengthRAW.split(" ")
                if lengthParts[1] == "A":
                    length = "18"
                elif lengthParts[1] == "About":
                    length = "24"
                elif lengthParts[1] == "3":
                    length = "3"
                else:
                    length = (int(lengthParts[1]) + int(lengthParts[3])) / 2

                lifeParts = lifeRAW.split(" ")
                life = (int(lifeParts[2]) + int(lifeParts[4]) )/2

                description = des1 + "\n" + des2
                arrayCats.append(Cats(name, description, weight, length, life, image))
    except:
        print("looking at ", os.getcwd())


Constructor()
print(arrayCats[0].GetCatDetails())
print(arrayCats[0].GetCatLife())
