def classification(value):
    if value == 2:
        return "Suspeito"
    elif 3 <= value <= 4:
        return "Cúmplice"
    elif value == 5:
        return "Assassino"
    return "Inocente"
cont = 0
p_1 = input().strip().upper()[0]
if p_1 == "S":
    cont += 1
p_2 = input().strip().upper()[0]
if p_2 == "S":
    cont += 1
p_3 = input().strip().upper()[0]
if p_3 == "S":
    cont += 1
p_4 = input().strip().upper()[0]
if p_4 == "S":
    cont += 1
p_5 = input().strip().upper()[0]
if p_5 == "S":
    cont += 1

print(classification(cont))
