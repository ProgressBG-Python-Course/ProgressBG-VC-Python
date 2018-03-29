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

# task 6
print("Distances bellow 1500km from Sofia are:")

for city in distances_from_sofia:
    if city[1] < 1500:
        print("{} - {}".format(city[0], city[1]))

# task 7
print()

for city in sorted(distances_from_sofia, key = lambda c: c[1]):
    if city[1] < 1500:
        print("{} - {}".format(city[0], city[1]))