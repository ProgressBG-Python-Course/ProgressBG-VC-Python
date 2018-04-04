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
  d = {}

  d[ "name" ] = input( "Enter your name: " )
  d[ "height" ] = cm_to_meters( float( input( "Enter your height in cm: " ) ) )
  d[ "weight" ] = float( input( "Enter your weight in kg: " ) )

  return d

def calc_BMI(w,h):
  """calculates the BMI

  Arguments:
    w {[float]} -- [weight]
    h {[float]} -- [height]

  Returns:
    [float] -- [calculated BMI = w / (h*h)]
  """
  return w / (h*h)

def calc_BMI_category(bmi):
  """Calculates the BMI category

  Arguments:
    bmi {[float]} -- [the bmi number index]

  Returns:
    [string] -- [bmi category]
  """
  pass

def print_results(bmi_category):
  """[Prints the BMI category to the user ]

  Arguments:
    bmi_category {[string]} -- []
  """
  pass

def cm_to_meters(cm):
  """converts centimetres to meters

  Arguments:
    cm {[int]}

  Returns:
    [float]
  """
  return cm/100

user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)