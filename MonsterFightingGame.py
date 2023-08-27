import random
monsterdict = {}
monster_fight_stats_comp = {}
monster_display_comp = {}
monster_fight_stats_user = {}
realname = False

def store():
    with open("Monsters.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            row = line.rstrip().split(",")
            monsterdict[row[1]] = row[0], row[2], row[3]
            monster_display_comp[row[0]] = row[1], row[2], row[3]
            monster_fight_stats_comp[row[0]] = row[4], row[5], row[6], row[7], row[8], row[9], row[10]
            monster_fight_stats_user[row[1]] = row[4], row[5], row[6], row[7], row[8], row[9], row[10]
store()

print("Which Monster to fight?")
searching = input("")
for key in monsterdict:
    if key == searching:
        print(monsterdict[key])
        realname = True

if realname == False:
    print("Not in Dictionary")

category = random.randint(0, 6)
print(category)

def fight():
    j = random.randint(1,895)
    i = str(j)
    print("Computer Picks", monster_display_comp[i])
    print("Computer Category Value is "+ monster_fight_stats_comp[i][category])
    print("Users Category Value is "+ monster_fight_stats_user[searching][category])
    if monster_fight_stats_comp[i][category] > monster_fight_stats_user[searching][category]:
        print("Computer Wins")
    if monster_fight_stats_comp[i][category] < monster_fight_stats_user[searching][category]:
        print("User Wins")
    if monster_fight_stats_comp[i][category] == monster_fight_stats_user[searching][category]:
        print("Draw")

if realname == True:
    fight()
