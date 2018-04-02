try:
	x = int( input("x = ") )
	y = int( input("y = ") )
	res = x/y
except Exception:
	print("Oopps")
except ValueError:
	print("You have not entered a number!!!")
except ZeroDivisionError:
	print("Can not divide by 0!!!")
else:
	print(res)









# print("End of program")

