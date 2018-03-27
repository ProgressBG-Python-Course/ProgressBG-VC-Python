# Input academical hour
acad_hours_input = int(input("Please, enter academical hours: "))

# break hour-each 4 academical hours there are 20 minutes break
acad_break = acad_hours_input/4

# break-20 min
break_one = 20

# all break 
break_hours = acad_break*break_one

# academical hour-40 min->h
acad_hours = int(input("Please, enter duration in minutes: "))

# how many astronomical hours a course should take
astronomical_hours_result = (acad_hours_input*acad_hours + break_hours)/60
print("astronomical hours a course take", astronomical_hours_result)

