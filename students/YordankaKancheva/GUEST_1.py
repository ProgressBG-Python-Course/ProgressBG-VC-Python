from random import randint
machine_number = randint(1,10)

#print("machine_number={}".format(machine_number))



tries = 0
while tries < 5:
    tries +=1
    y=int(input("Моля, отгатнете намисленото от мен число, което е от 1 до 10:\n"))
    if y > machine_number:
        print("Вашето предположение е по-голямо от намисленото от мен число.\n")
    elif y < machine_number:
        print("Вашето предположение е по-малко от намисленото от мен число.\n")
    elif y == machine_number:
        print("Поздравления, това е намисленото от мен число!")
        break
    if tries == 5:
        print("Вие загубихте. Намисленото число е " +format(machine_number)+".")
