import csv
with open('sample_data.csv') as f:
  f_csv = csv.reader(f)
  headers = next(f_csv)
  for row in sorted(f_csv, key=lambda a:a[0]):
      print(row)