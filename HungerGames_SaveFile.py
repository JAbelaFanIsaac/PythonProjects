import random

# Define the characteristics for Hunger Games characters
districts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
names = ["Katrina", "Jasper", "Elara", "Felix", "Iris", "Leo", "Maeve", "Orion", "Seraphina", "Theo", "Zara", "Darius"]
weapons = ["Sword", "Bow and Arrows", "Spear", "Knife", "Trident", "Axe", "Crossbow", "Mace", "Slingshot", "Whip"]
special_abilities = ["Stealth", "Climbing", "Swimming", "Tracking", "Camouflage", "Hand-to-hand combat", "Archery", "Strength", "Speed", "Intelligence"]

# Class definition for Hunger Games characters
class HungerGamesCharacter:
    def __init__(self):
        self.__district = random.choice(districts)
        self.__name = random.choice(names)
        self.__weapon = random.choice(weapons)
        self.__special_ability = random.choice(special_abilities)

    # Getters
    def get_district(self):
        return self.__district

    def get_name(self):
        return self.__name

    def get_weapon(self):
        return self.__weapon

    def get_special_ability(self):
        return self.__special_ability
    def printme(self):
        print("District:",self.__district)
        print("Name:",self.__name)
        print("Weapon:",self.__weapon)
        print("Special ability:",self.__special_ability)

# Generate a Hunger Games character object
character = HungerGamesCharacter()

# Use getters to access private attributes
print("Using getters:")
print("District:", character.get_district())
print("Name:", character.get_name())
print("Weapon:", character.get_weapon())
print("Special ability:", character.get_special_ability())

# Use the printme method
print("\nUsing printme method:")
character.printme()

# 1. So I'd like five new characters added to a list
# 2. Then save those characters to a text file. (Saving the attributes)

List_characters = []

for i in range(5):
    character_testing = HungerGamesCharacter()
    List_characters.append(character_testing)

print(List_characters)

#Putting it into A LIST
with open("Hunger_Characters.txt", "a") as file:
    for i in range(5):
        file.write(List_characters[i].get_district() + "\n")
        file.write(List_characters[i].get_name()+ "\n")
        file.write(List_characters[i].get_weapon()+ "\n")
        file.write(List_characters[i].get_special_ability()+ "\n")
        file.write("\n")
