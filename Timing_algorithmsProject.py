import datetime
start_time = datetime.datetime.now()

correct = 0
while correct < 5:
    answ = int(input("what is 2+2?"))
    if int(answ) == 4:
        correct = correct+1


time_taken = (datetime.datetime.now()-start_time)
print(time_taken.seconds)
average_time = time_taken/5
print(average_time.seconds)
