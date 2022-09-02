import random
Attack1 = [40, 40, 10, 10, 10, 10]
Attack2 = [20, 20, 20, 20, 20, 20]
Attack3 = [120, 0, 0, 0, 0, 0]
Attack4 = [10, 10, 10, 30, 30, 30]
P1A1 = 0
P1A2 = 0
P1A3 = 0
P1A4 = 0
P2A1 = 0
P2A2 = 0
P2A3 = 0
P2A4 = 0
Health1 = 100
Health2 = 100
while 0 < 1:
    P1Choice = int(input("P1: [1] Att 1, [2] Att 2, [3] Att 3, [4] Att 4,[5] Heal"))
    if P1Choice not in [1, 2, 3, 4, 5]:
        print("Not a valid option")
    if P1Choice == 1:
        damage1 = random.choice(Attack1)
        P1A1 = P1A1 + 1
        Health2 = Health2 - damage1
        print("P2 at HP", Health2)
    if P1Choice == 2:
        damage2 = random.choice(Attack2)
        P1A2 = P1A2 + 1
        Health2 = Health2 - damage2
        print("P2 at HP", Health2)
    if P1Choice == 3:
        damage3 = random.choice(Attack3)
        P1A3 = P1A3 + 1
        Health2 = Health2 - damage3
        print("P2 at HP", Health2)
    if P1Choice == 4:
        damage4 = random.choice(Attack4)
        P1A4 = P1A4 + 1
        Health2 = Health2 - damage4
        print("P2 at HP", Health2)
    if P1Choice == 5:
        Health1 = Health1 + 20
        print("P1 at HP", Health1)
    if Health2 <= 0:
        print("P1 Won")
        print("Att 1, Att 2, Att 3, Att 4:", P1A1, P1A2, P1A3, P1A4)
        break
    P2Choice = int(input("P2: [1] Att 1, [2] Att 2, [3] Att 3, [4] Att 4,[5] Heal"))
    if P2Choice not in [1, 2, 3, 4, 5]:
        print("Not a valid option")
    if P2Choice == 1:
        damage1 = random.choice(Attack1)
        P2A1 = P2A1 + 1
        Health1 = Health1 - damage1
        print("P1 at HP", Health1)
    if P2Choice == 2:
        damage2 = random.choice(Attack2)
        P2A2 = P2A2 + 1
        Health1 = Health1 - damage2
        print("P1 at HP", Health1)
    if P2Choice == 3:
        damage3 = random.choice(Attack3)
        P2A3 = P2A3 + 1
        Health1 = Health1 - damage3
        print("P1 at HP", Health1)
    if P2Choice == 4:
        damage4 = random.choice(Attack4)
        P2A4 = P2A4 + 1
        Health1 = Health1 - damage4
        print("P1 at HP", Health1)
    if P2Choice == 5:
        Health2 = Health2 + 20
        print("P2 at HP", Health1)
    if Health1 <= 0:
        print("P2 Won")
        print("Att 1, Att 2, Att 3, Att 4:", P2A1, P2A2, P2A3, P2A4)
        break