import os

arrayEmployees = []

def lowercase(text):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    outText = ""
    for letter in text:
        if letter in uppercase:
            index = uppercase.index(letter)
            outText = outText + lowercase[index]
        else:
            outText = outText + letter

    return outText

class employee():
    def __init__(self, first, second, count):
        self.__FirstName = first
        self.__LastName = second
        self.__FullName = first + " " + second
        email = lowercase(first) + "." + lowercase(second) + "@company.com"
        self.__Email = email
        self.__UniqueID = int(count)

    def ID(self):
        return self.__UniqueID

    def Email(self):
        return self.__Email

    def PrintDetailsFULL(self):
        message = self.__FirstName + " " + self.__LastName + " " + self.__FullName +\
                  " " + self.__Email + " " + str(self.__UniqueID)
        print(message)

    def PrintDetails(self):
        message = self.__FullName + " " + self.__Email + " " + str(self.__UniqueID)
        print(message)

def Constructor():
    try:
        with open("emailList.txt", "r") as file:
            for i in range(10):
                first = file.readline().strip()
                second = file.readline().strip()
                arrayEmployees.append(employee(first, second, str(i+1)))

    except:
        print("Looking at ", os.getcwd())

Constructor()
arrayEmployees[7].PrintDetails()

def GetEmployeeEmail(ID):
    Found = False
    for j in range(10):
        if int(arrayEmployees[j].ID()) == int(ID):
            Found = True
            print(arrayEmployees[j].Email())

    if Found == False:
        print("Not found")

GetEmployeeEmail(2)
