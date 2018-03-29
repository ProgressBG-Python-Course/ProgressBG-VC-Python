# Task 5
print('=' * 20)
print("Task 5")
print('=' * 20)

names = []
n = int(input("How many names are you going to enter? "))
if n >= 1:
  for i in range(n):
     names.append(input("Enter a name, please: "))
  print("****************************** \nThe names you've entered are:")
  for i in range(n):
     print(names[i])

