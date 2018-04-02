# BMI   Category
# <= 18.5  Underweight
# 18.5–24.9    Normal
# 25–29.9  Overweight
# >= 30    Obesity
user_name_lenght = 2
user_height_min = 50
user_height_max = 250
user_weight_min = 3
user_weight_max = 300

def cm_to_meters(cm):
  """converts centimetres to meters

      Arguments:
        cm {[int]}

      Returns:
        [float]
  """
  return cm/100.00

def validate_name(name):
    if len(name) >= user_name_lenght:
        return True
    return False

def validate_height(height):
    if height > user_height_min and height < user_height_max:
        return True
    return False

def validate_weight(weight):
    if weight > user_weight_min and weight < user_weight_max:
        return True
    return False

def get_user_data():
  """retrieves user data from the command line

      Returns:
        [dictionary] of the form:
          {
            "name" : "user_name",
            "height": "user heigth in meters",
            "weight": "user weight in kilograms"
          }
  """
  while True:
      name = input("Enter your name. At least 2 charters long: ")
      if validate_name(name):
          break

  while True:
      height = float(input("Enter your heigth in cm: "))
      if validate_height(height):
          height = cm_to_meters(height)
          break

  while True:
      weight = float(input("Enter your weight in kg: "))
      if validate_weight(weight):
          break

  user_data = {
    "name":name,
    "height":height,
    "weight":weight
  }
  return user_data

def calc_BMI(w,h):
  """calculates the BMI

      Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]

      Returns:
        [float] -- [calculated BMI = w / (h*h)]
  """
  return round( w / (h*h),2)

def calc_BMI_category(bmi):
  """Calculates the BMI category

      Arguments:
        bmi {[float]} -- [the bmi number index]

      Returns:
        [string] -- [bmi category]
  """
  if bmi <= 18.5:
      return 'Underweight'
  elif bmi >  18.5 and bmi <= 25:
      return "Normal"
  elif bmi > 25 and bmi <= 30:
      return "Overweight"
  elif bmi >30:
      return "Obesity"
  else:
      return "Unable to match category!!!"

def print_results(bmi_category):
  """[Prints the BMI category to the user ]
  Arguments:
    bmi_category {[string]} -- []
  """
  print("Your BMI Catergory is: ",bmi_category)


user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)