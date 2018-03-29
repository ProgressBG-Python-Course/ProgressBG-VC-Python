
number_of_names = int(input("How many names are you going to enter? "))
names = []
for i in range(number_of_names):
    names.append(input("Enter a name, please: "))

print(30*'*')
print("The names you've entered are:")

for n in names:
    print(n)
