import os
file_name = input("files")

def file_exists(names):
    try:
        with open(file_name, "r") as file:
            print("Looking at", os.getcwd())
            return True
    except:
        print("Not existent, looking at ", os.getcwd())
        return False

print(file_exists(file_name))
