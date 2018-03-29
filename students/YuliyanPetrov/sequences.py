def int_try_parse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False
#Task1

first_names =["ivan", "maria", "petar"]
sur_names =["ivanov", "popova", "petrov"]
both_names = first_names + sur_names
print(both_names)

#Task 2
first_names =["ivan", "maria", "petar"]
sur_names =["ivanov", "popova", "petrov"]

both_names = []
for i in range(len(first_names)):
    both_names.append(first_names[i])
    both_names.append(sur_names[i])
print(both_names)

#Task 3
sum=0
for i in range(1000,1201):
    if i%2==0:
        sum+=i
print(sum)
#Task 4
words = ["dog", "talent", "loop", "aria", "tent", "choice"]
print("Words which starts and end with same letter are:")

for w in words:
    if w[0] == w[-1]:
        print(w)

#Task 5
list_of_inputs = []
number_of_input = input("How many names are you going to enter? ")
number_of_input = int_try_parse(number_of_input)
number_of_input = number_of_input[0]

for n in range(number_of_input):
    name = input("Enter a name, please ")
    list_of_inputs.append(name)
print("The names you've entered are:")
for name in list_of_inputs:
    print(name)

#Task 6
distances_from_sofia = [
    ("Bansko", 97),
    ("Brussels", 1701),
    ("Alexandria", 1403),
    ("Nice", 1307),
    ("Szeged", 469),
    ("Dublin", 2479),
    ("Palermo", 987),
    ("Moscow", 1779),
    ("Oslo", 2098),
    ("London", 2019),
    ("Madrid", 2259),
]

short_distances_from_sofia = []
for d in distances_from_sofia:
    if d[1] <1500:
       record = (d[0],d[1])
       short_distances_from_sofia.append(record)

print("Distances bellow 1500km from Sofia are:")
for d in short_distances_from_sofia:
    print("{} - {}".format(d[0],d[1]))