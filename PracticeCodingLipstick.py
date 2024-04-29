arrayLipstick = []

class Lipstick():
    def __init__(self, name, price, comfort, pigment, wear, rating, shades, cruelty):
        self.__LipstickName = name
        self.__Price = float(price)
        self.__Comfort = float(comfort)
        self.__Pigment = float(pigment)
        self.__Wear = float(wear)
        self.__AmazonRating = float(rating)
        self.__Shades = int(shades)
        self.__CrueltyFree = cruelty

    def GetName(self):
        return self.__LipstickName

    def GetRating(self):
        return float(self.__AmazonRating)

    def ChangeRating(self, newValue):
        self.__AmazonRating = newValue

    def Check(self):
        message = self.__LipstickName + " " +str(self.__AmazonRating)
        return message

def ReadData():
    try:
        with open("LipstickData.txt", "r") as file:
            for i in range(6):
                name = file.readline().strip()
                price = file.readline().strip()
                comfort = file.readline().strip()
                pigment = file.readline().strip()
                wear = file.readline().strip()
                shades = file.readline().strip()
                cruelty = file.readline().strip()
                if str(cruelty) == "Yes":
                    text = True
                else:
                    text = False
                arrayLipstick.append(Lipstick(name, price, comfort, pigment, wear, 0.0, shades, text))
    except:
        print("Can't find the file")

ReadData()

arrayReviews = []

def GetReviews():
    try:
        with open("AmazonReview.txt", "r") as file2:
            for i in range(6):
                row = file2.readline().strip().split(", ")
                if len(row) == 1:
                    rating = float(input("Give rating: "))
                    name = row[0]
                else:
                    name = row[0]
                    rating = float(row[1])
                arrayReviews.append([name, rating])

    except:
        print("Can't find the file")

GetReviews()

def MatchingReviews():
    for item in range(6):
        for i in range(6):
            if arrayLipstick[item].GetName() == arrayReviews[i][0]:
                arrayLipstick[item].ChangeRating(float(arrayReviews[i][1]))

MatchingReviews()

def SortRanking():
    for count in range(1,5,1):
        i = count
        value = arrayLipstick[count]
        temp = value.GetRating()
        while i > 0 and temp > float(arrayLipstick[i-1].GetRating()):
            print(temp)
            print(float(arrayLipstick[i-1].GetRating()))
            arrayLipstick[i] = arrayLipstick[i-1]
            i = i-1
        arrayLipstick[i] = value

    print(arrayLipstick)

SortRanking()

for i in range(6):
    print(arrayLipstick[i].Check())
