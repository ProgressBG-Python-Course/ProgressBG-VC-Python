#BMI_Calculator
def float_try_parse(value):
    try:
        return float(value), True
    except ValueError:
        return value, False

#weight_in_kilogram = 100.00
#height_in_meters = 1.85
weight_in_kilogram = input("Input your weight in [KG] (98.5): ")
height_in_meters = input("Input your height in [m] (i.e 1.75): ")

weight_in_kilogram = float_try_parse(weight_in_kilogram)
height_in_meters = float_try_parse(height_in_meters)

if weight_in_kilogram[1]==False or height_in_meters[1]==False:
    print("Weight and height inputs should be numbers!!!")
else:
    if weight_in_kilogram[0] <=0 or height_in_meters[1]<=0:
        print("Weight and height should be possitive numbers!!! (greather than 0)")
    else:
        BMI = round( weight_in_kilogram[0] / (height_in_meters[0]*height_in_meters[0]),2)
        print("Your BMI is:",BMI)
