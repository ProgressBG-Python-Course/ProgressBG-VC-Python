class Person():
  age = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age


class Employee(Person):
  def __init__(self,name, age, salary):
    # Person.__init__(self,name, age)
    super().__init__(name, age)
    self.salary = salary


pesho = Employee("Pesho", 50, 400)

print( pesho.name )
print( pesho.salary )







