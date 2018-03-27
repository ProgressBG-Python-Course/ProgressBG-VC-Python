#guessTheNumber
from random import randint

def int_try_parse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def compare_machine_vs_user(user_imput,machine_number):
    if user_imput > machine_number:
        print("Your guess is bigger")
        return False
    elif user_imput < machine_number:
        print("Your guess is less")
        return False
    elif user_imput == machine_number:
        print("Congratulations - YOU WIN!!!!")
        return True
    else: return  False

def user_input():
    user_imput = int_try_parse(input("Guess Machine Number? \n"))
    if user_imput[1]== False:
        print("Please Enter number between 1-10")
    else:
        check = compare_machine_vs_user(user_imput[0],machine_number)
        return (check)

machine_number = randint(1,10)
print("machine_number={}".format(machine_number))

x=False
while x!=True:
    check = user_input()
    x=check