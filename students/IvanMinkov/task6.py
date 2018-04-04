# Task 6
print('=' * 20)
print("Task 6")
print('=' * 20)

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
dist_close_to_Sofia = []

for place in distances_from_sofia :
    if place[1] < 1500:
        dist_close_to_Sofia = dist_close_to_Sofia + [place]
print("OutputDistances bellow 1500km from Sofia are:")
for place in sorted(dist_close_to_Sofia, key=lambda dist_close_to_Sofia:dist_close_to_Sofia[1]):
    print("{} - {}".format(place[0],place[1]))


