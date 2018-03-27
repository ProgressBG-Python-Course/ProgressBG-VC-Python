from random import randint
machine_number = randint(1,10)
print("machine_number={}".format(machine_number))
tries = 5
while tries > 0 :
    user_number = int(input("Please, input a number between 1 an 10: "))
    if user_number == machine_number :
        print("Congratulations! You've guessed it!") 
        break
    elif user_number < machine_number :
	    print("Your guess is less than my number. Try again!")
    elif user_number > machine_number :
	    print("Your guess is greater than my number. Try again!")
    tries -=1
if tries == 0 :
    print("=" * 30,"\n Your loose! My number is {}.".format(machine_number))