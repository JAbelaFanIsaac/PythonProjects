import random
print("You are in captivity due to you and a friend hacking YouTube and demonetizating all Youtubers such as")
print("the Sideman, Pewdiepie and Click etc...")
print("YouTube still doesn't know which one hacked the system... You or your friend Jack....")
print("You are given the option to either confess or stay silent...")
print("If one of you stays silent and the other one confesses,")
print("the confessor is released from prison and the silent one is in prison for 20 years...")
print("If you both stay silent you are both in prison for only 1 year each...")
print("If you both confess then you are both in prison for 5 years each...")
print("Your friend Jack is in another room and there is no way to communicate with him...")
def play():
    q = input("What do you do? (Confess -> C, Silent -> S)")
    d = 0
    r = 1
    v = random.choice([d, r])
    if q == "C" and v == 0:
        print("You are both in prison for 5 years")
    if q == "C" and v == 1:
        print("You are free")
    if q == "S" and v == 0:
        print("You are in prison for 20 years")
    if q == "S" and v == 1:
        print("You are both in prison for 1 year")

while True:
    answer = input("Do you want to play?(y,n)")
    if answer == 'y':
        play()
    elif answer == 'n':
        break
    else:
        print("dont understand")