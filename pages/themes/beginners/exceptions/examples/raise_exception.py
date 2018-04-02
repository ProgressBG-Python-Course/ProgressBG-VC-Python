try:
	user_number = int(input("Enter a number: "))
except ValueError:
	print("~"*30)
	print("You did not enter a number!")
	print("~"*30)
	raise
