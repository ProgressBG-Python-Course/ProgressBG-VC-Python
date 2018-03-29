# Task 2
print('=' * 20)
print("Task 2")
print('=' * 20)

first_names = ["Ivan" , "Maria" , "Peter"]
sur_names = ["Ivanov", "Popova", "Petrov"]

names = []
for s in range(3):
		# iep: discuss: this (interpolates names on each iter) vs append
    names = names + [first_names[s]] + [sur_names[s]]
print (names)