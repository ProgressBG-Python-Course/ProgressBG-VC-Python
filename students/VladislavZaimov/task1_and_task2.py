first_names = [ "ivan", "maria", "petar"]
sur_names  =  ["ivanov", "popova", "petrov"]

# Task 1
names = first_names + sur_names
print(names)

# Task 2
names = []
for f, s in zip(first_names, sur_names):
    names.append(f)
    names.append(s)

print(names)

