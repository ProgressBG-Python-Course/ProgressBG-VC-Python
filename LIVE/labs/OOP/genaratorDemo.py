def evenNumbersGenerator(x):
  while True:
    x += 1
    yield x


  # yield 1
  # yield 2
  # yield 3
  # yield 4
  # yield 5
  # yield 6
  # yield 7



gen=evenNumbersGenerator(5)


print( next(gen) )
print( next(gen) )
print( next(gen) )
print( next(gen) )
