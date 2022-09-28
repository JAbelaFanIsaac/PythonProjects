import random
text = ""
for _ in range(9):
    a = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    text = text + a
print(text)
User = input("Repeat the text above.")
if User == text:
    print("Thank you")
else:
    print("Incorrect")
