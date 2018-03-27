import random

max_tries = 5

machine_num = random.randint(1,10)
print('machine number: {}'.format(machine_num))
tries = 1
while tries <= max_tries:
    user_number = int(input("Guess the number between 1 and 10 > "))
    if user_number < machine_num:
        print("your number is less than mine")
    elif user_number > machine_num:
        print("your number is more than mine")
    else:
        print("Congratulations!")
        break
    tries += 1
print('Game over')