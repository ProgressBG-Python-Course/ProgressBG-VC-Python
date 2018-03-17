users = (
    ["Ivan", "Ivanov", 34],
    ["Maria", "Ivanova", 36],
    ["Asen", "Asenov", 20],
)

### try to change a tupple item:
# users[0] = 5
# # TypeError: 'tuple' object does not support item assignment

### try to change a tupple item:
# users[0] = ["Petyr", "Petrov", 45]
# # TypeError: 'tuple' object does not support item assignment

### try to change items inside a mutable tuple item:
users[0][2] = 100
users[1][2] = 100
users[2][2] = 100
print(users)
# (['Ivan', 'Ivanov', 100], ['Maria', 'Ivanova', 100], ['Asen', 'Asenov', 100])

