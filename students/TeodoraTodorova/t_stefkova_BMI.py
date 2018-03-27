# Input academical hour
weight_in = float(input("Please, enter your weight in kilogram: "))
weight_in_kilogram = round(weight_in, 2)

# break hour-each 4 academical hours there are 20 minutes break
height_in = float(input("Please, enter your height in meters: "))
height_in_meters = round (height_in, 2)

#body mass index (BMI)
BMI = round (weight_in_kilogram / (height_in_meters**2), 2)
print("Your body mass index (BMI) is ", BMI)

# for BMI in range (0, 18.5, 0.5)
#     print ("Your body mass index (BMI) is Underweight ", BMI)
#     for BMI in range (18.5, 24.9, 0)
#         print ("Your body mass index (BMI) is Normal ", BMI)
#         return


# BMI	Category
# <= 18.5	Underweight
# 18.5–24.9	Normal
# 25–29.9	Overweight
# >= 30	Obesity

