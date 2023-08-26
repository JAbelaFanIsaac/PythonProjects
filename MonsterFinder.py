monsterdict = {}
realname = False

def store():
    with open("filetomain.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            name, description = line.rstrip().rsplit(",")
            monsterdict[name] = description
store()
print("Info about which monster?")
searching = input("")
for key in monsterdict:
    if key == searching:
        print(monsterdict[key])
        realname = True

if realname == False:
    print("Not in Dictionary")
