list1=[]
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
print("\nDistances bellow 1500 km from Sofia are:\n") 
for i in distances_from_sofia:
    if i[1] < 1500:
        list1.append(i)
print(list1,"\n")
