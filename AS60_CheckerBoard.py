n = int(input("Width"))
m = int(input("Length"))
alt = n//2
height = m//2
linea = (".", "*")*alt
lineb = ("*", ".")*alt
if n%2 == 0:
    if m%2 == 0:
        for i in range(height):
            print(linea)
            print(lineb)
    if m%2 == 1:
        for i in range(height):
            print(linea)
            print(lineb)
        print(linea)
if n%2 == 1:
    if m%2 == 0:
        for i in range(height):
            print(linea, ".")
            print(lineb, "*")
    if m%2 == 1:
        for i in range(height):
            print(linea, ".")
            print(lineb, "*")
        print(linea, ".")