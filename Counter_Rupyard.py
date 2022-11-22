first_total = 0
second_total = 0

with open("C:/Users/201036/PycharmProjects/Y12/venv/if.txt", "r") as file1:
    for i in file1:
        first_lower = i.count(" if ")
        first_higher = i.count("If")
        first_quote = i.count("'if'")
        first_total = first_total + first_lower + first_higher + first_quote
print(first_total)

with open("C:/Users/201036/PycharmProjects/Y12/venv/mam.txt", "r") as file2:
    for line in file2:
        second_lower = line.count(" if ")
        second_higher = line.count("If")
        second_quote = line.count("'if'")
        second_total = second_total + second_lower + second_higher + second_quote
print(second_total)

if first_total > second_total:
    print("Male>Female")
if first_total < second_total:
    print("Female<Male")
