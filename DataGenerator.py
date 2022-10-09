import random
import datetime
char = random.randint(33, 127)
range_repeat = random.randint(1, 10)

def create_char():
    output = chr(char)
    print(output)

def create_integer():
    output = random.randint(1, 10000)
    print(output)

def create_real():
    output = random.uniform(1, 10000)
    print(output)

def create_string():
    output = ''
    value = random.randint(65, 122)
    while value < 97 and value >90:
        value = random.randint(65, 122)
        if value < 90 or value > 97:
            break
    first_char = chr(value)
    output = output + first_char
    for i in range(range_repeat):
        reps = random.randint(33, 127)
        new = chr(reps)
        output = output + new
    print(output)

def create_date():
    start_dt = datetime.date(2000, 1, 1)
    end_dt = datetime.date(2022, 12, 31)
    time_between_dates = end_dt - start_dt
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_dt + datetime.timedelta(days=random_number_of_days)
    print(random_date)

def create_boolean():
    decide = random.randint(1, 2)
    if decide == 1:
        print("True")
    else:
        print("False")
