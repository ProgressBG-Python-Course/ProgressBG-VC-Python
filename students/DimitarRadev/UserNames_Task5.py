# iep: discuss - upper case variable name
Num_tries = input("How many names are you going to enter:")
tries = 0
list = []
# iep: discuss Num_tries || 3 ?
while tries < Num_tries:
    y=str(input("Enter a name, please:\n"))
    list.append(y)
    tries += 1
    if tries == 3:
        print("The names you've entered are:" , list)