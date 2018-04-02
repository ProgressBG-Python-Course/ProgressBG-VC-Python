x = 999

def foo():
	global x
	x = 5

	print("x in foo() = ", x)


print(" x in global: ", x)