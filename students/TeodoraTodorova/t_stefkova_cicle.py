### machine number:
from random import randint
number_machine = randint(1,10)
# print("number_machine={}".format(number_machine))

### If the user guess is equal to the machine number => print out a congratulation message!
number_guest=int(input("Въведи цяло число от 1 до 10: "))

while (number_guest != number_machine):
    if number_guest > number_machine:
        number_guest=int(input("Опитай отново с цяло по-малко число от 1 до 10: "))
    elif number_guest < number_machine:
        number_guest=int(input("Опитай отново с цяло по-голямо число от 1 до 10: "))
else:
    print ("Поздравления, ти позна числото!")
