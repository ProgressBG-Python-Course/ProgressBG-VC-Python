#define class Student
class Students():
  def __init__(self,name, sur_name, age):
    self.__name = name
    self.__sur_name = sur_name
    self.__age = age

  def __str__(self):
    return "{} - {}".format(self.__name, self.__age)

  def set_age(self, password, age):
    if password == "sezam":
      # validate age: must be [0-101]
      self.__age = age



  def get_age(self):
    return self.__age

# create Student objects
maria=Students("Maria", "Popova", 20)
pesho=Students("Pesho", "Popov", 30)

# use Student objects
# Maria's age before change
print( maria.get_age() )

# Change Maria's age:
maria.set_age("sezam", 1000)

# Maria's age after change
print( maria.get_age() )