num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sumlist(num):
    total = 0
    for i in range(len(num)):
        total = total + num[i]
    return total

def productlist(num):
    total = num[0]
    for i in range(len(num)-1):
        total = total * num[i+1]
    return total
