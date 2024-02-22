array = [45, 34, 2, 67, 89, 37, 80]

class node:
    def __init__(self, data):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    def insert(self, data):
        if data < self.__data:
            if self.__leftChild:
                self.__leftChild.insert(data)
            else:
                self.__leftChild = node(data)
                return

        else:
            if self.__rightChild:
                self.__rightChild.insert(data)
            else:
                self.__rightChild = node(data)
                return

    def search(self, val):
        if val == self.__data:
            return str(val) + " is found in BST"
        elif val < self.__data:
            if self.__leftChild:
                return self.__leftChild.search(val)
            else:
                return str(val)+ " not found in BST"
        else:
            if self.__rightChild:
                return self.__rightChild.search(val)
            else:
                return str(val)+ " not found in BST"

    def PrintTree(self):
        if self.__leftChild:
            self.__leftChild.PrintTree()
        print(self.__data)
        if self.__rightChild:
            self.__rightChild.PrintTree()

root = node(27)
for i in range(7):
    root.insert(array[i])

root.PrintTree()

print(root.search(78))
print(root.search(80))

