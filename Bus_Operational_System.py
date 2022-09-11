while 0 < 1:
    #Lists used in this code
    bus_time = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
    bus_capacity = [40, 40, 40, 40, 40, 40, 40, 64]
    bus_money = [0, 0, 0, 0, 0, 0, 0, 0]
    charge=15
    
    bus_choice = int(input("\nChoose your Bus. Please enter 09:00 [0],11:00 [2],13:00 [4] or 15:00 [6]: "))
    # Generates an integer which we can then use to access the correct data.
    print("Bus time chosen:",bus_time[bus_choice])
    # Notice how the data inputted can now retrieve the list items.
    if bus_choice not in [0, 2, 4, 6]:
        print("Not a valid bus to KL City Centre.")
    # Very simple validation to make sure do not choose bus coming back.
    bus_capacity[bus_choice]= bus_capacity[bus_choice] - 1
    bus_money[bus_choice] += charge
    #Adjusts lists to take ticket away.
    Continue = int(input("Buy a return ticket? Please enter YES [1],NO [0]"))
    if Continue != 1:
        break
    bus_return = int(input("\nChoose your Bus. Please enter 10:00 [1],12:00 [3],14:00 [5] or 16:00 [7]: "))
    # Generates an integer which we can then use to access the correct data.
    print("Bus time chosen:",bus_time[bus_return])
    if bus_return not in [1, 3, 5, 7]:
        print("Not a valid bus to KL City Centre.")
    # Very simple validation to make sure do not choose bus coming back.
    bus_capacity[bus_return]= bus_capacity[bus_return] - 1
    bus_money[bus_return] += charge
    #Adjusts lists to take ticket away.
    break

print("\nUpdated Lists")
print("Bus Times",bus_time)
print("Bus capacity", bus_capacity)
print("Bus money", bus_money)
# Printed to show you how the lists have changed.