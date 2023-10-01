import csv

with open('./Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)
    for row in csvreader:
            print(row[0], row[1])