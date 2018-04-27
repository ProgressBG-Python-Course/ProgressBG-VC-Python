import pandas as pd

### creation
# data = pd.Series([1,2,3,4])


### indexing
# data = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])

### Series as specialized dictionary
# prices = {
#   "apples": 1.5,
#   "oranges": 2.3,
#   "bananas": 2.5
# }
# data = pd.Series(prices)

### Series slicing
prices = {
  "apples": 1.5,
  "oranges": 2.3,
  "bananas": 2.5,
  "strawberies": 3.5
}
data = pd.Series(prices)
print(data["apples":"bananas"])


# print(data)
