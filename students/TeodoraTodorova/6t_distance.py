# Write a program, which will outputs only the distances from Sofia which are bellow 1500km
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

for d in distances_from_sofia:
    if d[-1] <= 1500:
        # print("{} - {} ".format(d[0], d[-1]))
        # print("{:10s}".format("=" * 30))
        # iep :discuss on sorted
        print( sorted( set(distances_from_sofia, key=d[-1] )) )
    else:
        pass