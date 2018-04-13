class Person():
  @staticmethod
  def validate_age(age):
    try:
      if not 0 < age < 100:
        raise ValueError("Invalid age value")
      else:
        return True
    except ValueError as e:
      print(e)

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "{}: {}".format(self.name, self.age)


maria = Person("Maria", 20)
pesho = Person("Pesho", 300)

print(maria)
maria.validate_age()
print(pesho)