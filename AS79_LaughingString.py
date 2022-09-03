count = 0
Vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
output = []
enter = input("String ")
repeater = len(enter)

def make_it_laugh():
    for count in range(repeater):
        if enter[count] in Vowels:
          output.append("haha")
          count = count + 1
        else:
            output.append(enter[count])
            count = count + 1
    constructor()

def constructor():
    Final = ""
    finalcount = 0
    for i in range(repeater):
        Final = Final + output[finalcount]
        finalcount = finalcount + 1
    print(Final)

make_it_laugh()
