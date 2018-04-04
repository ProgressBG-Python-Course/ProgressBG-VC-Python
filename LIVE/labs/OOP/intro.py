class Person:
	eye_count = 2
	first_name = "None"

	def __init__(self,first_name, last_name,age ):
		self.first_name = first_name
		self.last_name = last_name
		self.__age = age


	def __greet__(self):
		print ("{} - {}".format(self.first_name, self.__age))



maria = Person("Maria", "Popova", 30)
pesho = Person("Pesho", "Petrov",50)

maria.__age = 100
maria.alaab

print( dir(maria) )