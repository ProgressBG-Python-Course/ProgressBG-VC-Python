
def get_user_data():
  dict = {}
  Name = ""
  Height = 0
  Weight = 0
  while (len(Name)<3 or (Height<50 and Height>250) or (Weight<5 and Weight>300)):
    Name = input("Enter your user name:")
    Height = int(input("Enter your hight:"))
    Weight = int(input("Enter your weight:"))
    
  dict["Name"] = Name
  dict["Height"] = Height
  dict["Weight"] = Weight
  
  return dict

def cm_to_meters(cm):
  return cm/100

def calc_BMI():
  a = get_user_data()
  result = a["Weight"] / (cm_to_meters(a["Height"])*cm_to_meters(a["Height"]))
  return result

BMI = calc_BMI()
def calc_BMI_category(BMI):
  if BMI <= 18.5:
    print("You are Underweight")
  elif BMI >= 18.5 and BMI <= 24.9:
    print("You are Normal")
  elif BMI >=25 and BMI <= 29.9:
    print("You are Overweight")
  elif BMI >= 30:
    print("Ypu are Obesity")
  else:
    print("Idon't know")
calc_BMI_category(BMI) 
  

  






  

