import os
import csv

budget_csv = os.path.join ( 'Resources', 'budget_data.csv')

with open(budget_csv) as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=',')
    num_rows = 0
    total = 0

    for row in csv_reader:
        
        if num_rows > 0:
            total = total + int(row[1])

        num_rows += 1

    print(f'Total Months: {num_rows - 1}')
    print(f'Total:$ {total}')
