#define class Student
class Students():
  count = 0
  def __init__(self,name, sur_name, age):
    self.__name = name
    self.__sur_name = sur_name
    self.__age = age

  def __str__(self):
    return "__str__ was called!"

  def __repr__(self):
    return "__repr__ was called!"


# create Student objects
maria=Students("Maria", "Popova", 20)
# pesho=Students("Pesho", "Popov", 30)

print( dir(maria) )
print( dict(Students) )
