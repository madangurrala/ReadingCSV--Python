import csv
import pandas

with open('address - address.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f'\t{row["First name"]} {row["Last name"]}')
