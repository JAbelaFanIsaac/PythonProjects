MathLine = {}

def readData():
   j= 1
   try:
       with open("TreasureChestData.txt", "r") as file:
           lines = file.readlines()
           for i in range(5):
               question = lines[3*i].replace("\n", '')
               answer = lines[3*i+1].replace("\n", '')
               points = lines[3*i+2].replace("\n", '')
               MathLine[j] = question, answer, points
               j = j + 1
       print(MathLine)
   except:
       print("File does not exist")

readData()
