"""
acad_to_astro_hours_with_vars.py

An example of too many variables, with too long names.


"""

# given:
minutes_in_astro_hour = 60
minutes_in_acad_hour = 40
acad_course_hours = 64
acad_hours_in_a_partida = 4

# program logic: 
acad_hours_partidas = acad_course_hours/acad_hours_in_a_partida

total_minutes_brakes = acad_hours_partidas * 20

minutes_in_a_course = acad_course_hours * minutes_in_acad_hour + total_minutes_brakes

course_in_astro_hours = minutes_in_a_course / 60

print(course_in_astro_hours)



