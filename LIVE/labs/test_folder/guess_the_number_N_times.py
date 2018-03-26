from random import randint
machine_number = randint(1,10)
print("machine_number={}".format(machine_number))

max_tries = 2
user_tries = 1

for i in range(max_tries):
	user_tries =+ 1

	user = int(input("Input your number:"))

	if user == machine_number:
	  print("Congratulations")
	  break
	elif user < machine_number:
	    print("your guess is less than my number. Try again")
	elif user > machine_number:
	    print("Your guess is greater than my number. Try again")
	else:
		pass

if max_tries==0:
	print("!!!You loose! My number is {}".format(machine_number))


