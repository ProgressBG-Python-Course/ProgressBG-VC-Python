
def calc_BMI(w,h):
  """calculates the BMI

  Arguments:
    w {[float]} -- [weight]
    h {[float]} -- [height]

  Returns:
    [float] -- [calculated BMI = w / (h*h)]
  """
  return round(w/(h*h),2)




def cm_to_meters(h_in_cm):
  """converts centimetres to meters

  Arguments:
    cm {[int]}

  Returns:
    [float]
  """ 
  return (round(h_in_cm/100,2))

def check_name_lenght(n):
  return len(n) < 2

def check_weight_range(w):
  return (w < 5 or w > 300)

def check_height_range(h):
  return (h < 50 or h > 250)

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
  
   usr_name = (input("Please input your name: "))
   while check_name_lenght(usr_name) :
     print("User name is too short. Please input at least 2 characters!")
     usr_name = (input("Please input your name: "))
   weight_in_kg = int(input("Please input your weight(kg): "))
   while check_weight_range(weight_in_kg) :
     print("Your weight is out of range 5 - 300 kg.")
     weight_in_kg = int(input("Please input your weight again: "))
   height_in_cm = int(input("Please input your height(cm): "))
   while check_height_range(height_in_cm):
     print("Your height is out of range 50 - 250 cm.")
     height_in_cm = int(input("Please input your height again: "))
   usr_data = {}
   usr_data['name'] = usr_name
   usr_data['height'] = cm_to_meters(height_in_cm)
   usr_data['weight'] = weight_in_kg
   return usr_data

    


def calc_BMI_category(a):
  """Calculates the BMI category

  Arguments:
    a [float] -- [the bmi number index]

  Returns:
    [string] -- [bmi category]
  """
  if a <= 18.50:
    return ('Underweight')
  elif a < 24.99:
    return ('Normal')
  elif a < 29.99:
    return ('Overweight')
  else:
    return ('Obesity')

def print_results(name,cat):
  """[Prints the BMI category to the user ]

  Arguments:
    name {[string]} -- []
    cat {[string]} -- []
  """
  print("{}, you are in the category of {}.".format(name,cat))


user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(user_data["name"],bmi_category)
