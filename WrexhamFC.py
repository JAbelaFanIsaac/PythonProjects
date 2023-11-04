import os

arrayPlayers = []

class Player():
    def __init__(self, number, first, second, position):
        self.__number = number
        self.__forename = first
        self.__surname = second
        self.__position = position
        self.__community = 0
        self.__injured = False

    def GetPlayerInfo(self):
        message = self.__forename + " " + self.__surname + ", " + self.__position
        return message

    def ChangeInjured(self):
        if self.__injured == False:
            self.__injured = True
        else:
            self.__injured = False

    def FullPlayerInfo(self):
        message = self.__forename + " " + self.__surname + ", " + self.__position +\
                  " " + self.__number + ' ' + str(self.__community) + " " + str(self.__injured)
        return message

    def ChangeCommunityInvolvement(self, value):
        self.__community = int(value)

def Constructor():
    try:
        with open("wrexham.txt", "r") as file:
            for i in range(28):
                num = file.readline().strip()
                first = file.readline().strip()
                second = file.readline().strip()
                position = file.readline().strip()
                arrayPlayers.append(Player(num, first, second, position))
    except:
        print("Cant find, looking at ", os.getcwd())

Constructor()
print(arrayPlayers[0].GetPlayerInfo())
