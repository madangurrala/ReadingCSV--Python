import csv

with open('address - address.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row["Province"] == "Ontario" :
            print(f'\t{row["First name"]} {row["Last name"]}')
