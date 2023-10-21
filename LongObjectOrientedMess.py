import random
Marking = 19

class Character:
    def __init__(self):
        self.name = ''
        self.attack = 0
        self.defense = 0
        self.health = 1
        self.experience = 0

    def print_basics(self):
        print("Name: ", self.name)
        print("Attack: ",self.attack)
        print("Defense: ", self.defense)
        print("Health: ", self.health)
        print("Experience: ", self.experience)

    def print_me(self):
        self.print_basics()

    def print_intro(self):
        print("This is an exciting story")

class wizard(Character):
    def __init__(self):
        Character.__init__(self)
        self.magic = 0

    def setter(self, name):
        self.name = name
        self.attack = random.randint(1,20)
        self.defense = random.randint(1, 20)
        self.health = random.randint(1, 20)
        self.experience = random.randint(1, 20)
        self.__money = random.randint(1,20)
        self.armour = 30

    def health_getter(self):
        return self.__money

    def print_me(self):
        self.print_basics()
        print("Magic: ", self.magic)

    class weapon:
        def attack():
            print("Waved the wand")
            j = random.randint(1, 20)
            if j == 20:
                print("Crit 20")
                return 12
            elif j > 7:
                print("Landed a hit")
                return 4
            elif j > 1:
                print("Miss")
                return 0
            if j ==1:
                print("Natural 1")
                return -1
        def defense():
            j = random.randint(1, 20)
            if j == 20:
                print("Crit 20")
                return 6
            elif j > 8:
                print("Armour up")
                return 2
            elif j > 1:
                print("Miss")
                return 0
            if j ==1:
                print("Natural 1")
                return -1
        def special():
            j = random.randint(1, 20)
            if j == 20:
                print("Crit 20")
                return 5
            elif j > 5:
                print("Landed a hit")
                return 1
            elif j > 1:
                print("Miss")
                return 0
            if j ==1:
                print("Natural 1")
                return -1


class knight(Character):
    def __init__(self):
        Character.__init__(self)
        self.armour = 0

    def setter(self, name):
        self.name = name
        self.attack = random.randint(1,20)
        self.defense = random.randint(1, 20)
        self.health = random.randint(1, 20)
        self.experience = random.randint(1, 20)
        self.__money = random.randint(1,20)
        self.armour = 30

    def health_getter(self):
        return self.__money

    def print_me(self):
        self.print_basics()
        print("Armour: ", self.armour)

    class weapon:
        def attack():
            print("Swing sword")
            j = random.randint(1, 20)
            if j == 20:
                print("Crit 20")
                return 8
            elif j > 7:
                print("Landed a hit")
                return 3
            elif j > 1:
                print("Miss")
                return 0
            if j == 1:
                print("Natural 1")
                return -1

        def defense():
            j = random.randint(1, 20)
            if j == 20:
                print("Crit 20")
                return 6
            elif j > 8:
                print("Armour up")
                return 2
            elif j > 1:
                print("Miss")
                return 0
            if j == 1:
                print("Natural 1")
                return -1

        def special():
            j = random.randint(1, 20)
            if j == 20:
                print("Crit 20")
                return 5
            elif j > 5:
                print("Landed a hit")
                return 1
            elif j > 1:
                print("Miss")
                return 0
            if j == 1:
                print("Natural 1")
                return -1

class hakari(Character):
    def __init__(self):
        Character.__init__(self)

    def setter(self, name):
        self.name = name
        self.attack = random.randint(1,20)
        self.defense = random.randint(1, 20)
        self.health = random.randint(1, 20)
        self.experience = random.randint(1, 20)
        self.__money = random.randint(1,20)

    def health_getter(self):
        return self.__money

    def print_me(self):
        self.print_basics()

    class weapon:
        def attack():
            print("Just one more")
            j = random.randint(1, 20)
            if j > Marking:
                print("Crit 20")
                return 90
            elif j >= 1:
                print("Miss")
                return 0

        def defense():
            j = random.randint(1, 20)
            if j == 20:
                print("Crit 20")
                return 10
            elif j > 5:
                print("Right back at ya")
                return 2
            elif j > 1:
                print("Miss")
                return 0
            if j == 1:
                print("Natural 1")
                return -2

        def special():
            j = random.randint(1,2)
            if j == 1:
                print("Success")
                return 20
            if j == 2:
                print("Loss")
                return -20

Name1 = input("What is your name?")
Class1 = int(input("Class?"))
Name2 = input("What is your name?")
Class2 = int(input("Class?"))

if Class1 == 1:
    Starting1 = knight()
    Starting1.setter(Name1)
if Class1 == 2:
    Starting1 = wizard()
    Starting1.setter(Name1)
if Class1 == 3:
    Starting1 = hakari()
    Starting1.setter(Name1)

if Class2 == 1:
    Starting2 = knight()
    Starting2.setter(Name2)
if Class2 == 2:
    Starting2 = wizard()
    Starting2.setter(Name2)
if Class2 == 3:
    Starting2 = hakari()
    Starting2.setter(Name2)

print(vars(Starting1))
print(vars(Starting2))
i = 1

def fight(person, i):
    b = input("A, D, H")
    if b == "A":
        if i % 2 == 0:
            bench = Starting2.weapon.attack()
            Starting1.health = Starting1.health - bench
        if i % 2 == 1:
            bench = Starting1.weapon.attack()
            Starting2.health = Starting2.health - bench
    if b == "D":
        if i % 2 == 0:
            bench = Starting2.weapon.defense()
            Starting2.health = Starting2.health + bench
        if i % 2 == 1:
            bench = Starting1.weapon.defense()
            Starting1.health = Starting1.health + bench
    if b == "H":
        if i % 2 == 0:
            bench = Starting2.weapon.special()
            Starting2.health = Starting2.health + bench
        if i % 2 == 1:
            bench = Starting1.weapon.special()
            Starting1.health = Starting1.health + bench
    if b == "XXX":
        print(vars(Starting1))
        print(vars(Starting2))
        print(Marking)
    i = i + 1
    if Starting1.health <= 0:
        print("Player 2 Wins")
        return 0
    if Starting2.health <= 0:
        print("Player 1 Wins")
        return 0
    else:
        if i % 2== 0:
            fight(Starting2, i)
        if i % 2 == 1:
            fight(Starting1, i)

fight(Starting1, i)
