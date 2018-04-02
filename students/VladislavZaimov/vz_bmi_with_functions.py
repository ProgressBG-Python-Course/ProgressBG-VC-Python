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

    while True:
        try:
            d[ "name" ] = input( "Enter your name: " )
            d[ "height" ] = cm_to_meters( float( input( "Enter your height in cm: " ) ) )
            d[ "weight" ] = float( input( "Enter your weight in kg: " ) )
        except ValueError:
            print ( "Please enter a number for height and weight!" )
        else:
            if not valid_height(d[ "height" ]):
                print("height must be between 50 and 250")
            elif not valid_weight( d[ "weight" ] ):
                print("weight must be between 5 and 300")
            elif not valid_name(d["name"]):
                print("Your name must be at least 2 characters long")
            else:
                break
    return d


def valid_name(name):
    return len(name) >= 2


def valid_height(height):
    return height >= 0.5 and height <= 2.5


def valid_weight(weight):
    return weight >= 5 and weight  <= 300


def calc_BMI(w, h):
    """calculates the BMI

    Arguments:
      w {[float]} -- [weight]
      h {[float]} -- [height]

    Returns:
      [float] -- [calculated BMI = w / (h*h)]
    """
    # print("BMI ",w / (h*h))
    return w / (h*h)


def calc_BMI_category(bmi):
    """Calculates the BMI category

    Arguments:
      bmi {[float]} -- [the bmi number index]

    Returns:
      [string] -- [bmi category]
    """
    if bmi <= 18.8:
        category = 'Underweight'
    elif bmi > 18.5 and bmi <= 24.9:
        category = 'Normal'
    elif bmi > 25 and bmi <= 29.9:
        category = 'Overweight'
    else:
        category = 'Obesity'
    return category


def print_results(bmi_category):
    """[Prints the BMI category to the user ]

    Arguments:
      bmi_category {[string]} -- []
    """
    print("Your BMI category is {}".format(bmi_category))


def cm_to_meters(cm):
    """converts centimetres to meters

    Arguments:
      cm {[int]}

    Returns:
      [float]
    """
    return float(cm)/100.0


user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)