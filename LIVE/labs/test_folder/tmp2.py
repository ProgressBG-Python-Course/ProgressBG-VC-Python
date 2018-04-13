class Test(object):
  'docstring for Test'
  def __init__(self, name, age):
    super(Test, self).__init__()
    self.name = name
    self.age = age


print( help(Test))