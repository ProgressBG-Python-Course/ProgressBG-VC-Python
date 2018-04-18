class EvenNumbersIterable():
  def __init__(self, count):
    self.count = count
    self.i = 0
    self.num = 0

  def __next__(self):
    if self.i < self.count:
      self.i += 1
      self.num += 2
      return self.num
    else:
      raise StopIteration


  def __iter__(self):
    return self



def evenNumbersGenerator(x):
  yield x
  print(x)
  x +=2

numbers = evenNumbersGenerator(0)

for i in numbers:
  print(i)


