from random import randint
machine_number = randint(1,10)
print("machine_number={}".format(machine_number))
user = int(input("Input your number:"))
if user == machine_number:
    print("Congratulations")
elif user < machine_number:
    print("your guess is less than my number. Try again")
elif user > machine_number:
    print("Your guess is greater than my number. Try again")
