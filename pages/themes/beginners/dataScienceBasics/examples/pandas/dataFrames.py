import pandas as pd

prices_dict = {
  "apples": 1.5,
  "oranges": 2.3,
  "bananas": 2.5,
  "strawberies": 3.5
}

suppliers_dict = {
  "apples":"applesSupplier",
  "oranges":"orangesSupplier",
  "bananas":"bananasSupplier",
  "strawberies":"strawberiesSupplier",
}


### Constructing DataFrame
## from  a Series object:
prices_ds = pd.Series(prices_dict)
suppliers_ds = pd.Series(suppliers_dict)


# prices_df = pd.DataFrame(prices_ds, columns=["prices"])
# suppliers_df = pd.DataFrame(suppliers_ds, columns=["suppliers"])

# print(prices_df, suppliers_df)

##  from  a multiple Series objects
fruits_df = pd.DataFrame({
  "proces": prices_ds,
  "suppliers": suppliers_ds
})
print(fruits_df)

