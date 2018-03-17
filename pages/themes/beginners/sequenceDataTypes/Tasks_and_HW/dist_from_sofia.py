distances_from_sofia = [
    ('Bansko', 97),
    ('Belgium - Brussels', 1701),
    ('Egypt - Alexandria', 1403),
    ('France - Nice', 1307),
    ('Hungary - Szeged', 469),
    ('Ireland - Dublin', 2479),
    ('Italy - Palermo', 987),
    ('Norway - Oslo', 2098),
    ('Russia - Moscow', 1779),
    ('Spain - Madrid', 2259),
    ('United Kingdom - London', 2019)
]

selected_distances = []
for t in distances_from_sofia:
    if(t[1] < 1500):
        selected_distances.append(t)

print("Distances bellow 1500 km from Sofia are:")
for t in selected_distances:
    print("{} - {}".format(t[0], t[1]))
