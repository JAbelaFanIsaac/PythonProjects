MyArray=["a", "b", "c", "d", "e", "f", "g"]
Found = False
Index = 0
item = input("What do you need to find?")

while Index < len(MyArray) and Found == False:
    if MyArray[Index] == item:
        print("Found item at position", Index)
        Found = True
    Index = Index + 1

if Found == False:
    print("Can't find the item")