import os
import csv

budget_csv = os.path.join ( 'Resources', 'budget_data.csv')

# Tasks;
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period

with open(budget_csv) as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=',')
    num_rows = 0
    total = 0
    month = []
    data = []
    for row in csv_reader:
        
        if num_rows > 0:
            total = total + int(row[1])
            month.append (row[0])
            data.append (int(row[1]))

        num_rows += 1
    
    i = 0
    diff = []
    while i < len(data) - 1:
        diff.append (data[i+1] - data[i])
        i = i + 1

    sum = 0
    j = 0
    while j < len(diff):
        sum = sum + diff[j]
        j = j + 1

    average = '{:.2f}'.format( sum / len(diff) )

    index_of_max = diff.index(max(diff))
    index_of_min = diff.index(min(diff))

    month_of_max = month[index_of_max+1]
    month_of_min = month[index_of_min+1]

    print(f'Total Months: {num_rows - 1}')
    print(f'Total:$ {total}')
    #print(f'Data: {data}') 
    #print(f'Data Length: {len(data)}') 
    #print(f'Diff: {diff}') 
    #print(f'Diff Length: {len(diff)}') 
    #print(f'sum: {sum}') 
    print(f'Average Change: {average}')
    #print(f'index_of_max: {index_of_max}') 
    #print(f'index_of_min: {index_of_min}') 
    #print(f'month_of_max: {month_of_max}') 
    #print(f'month_of_min: {month_of_min}')
    print(f'Greatest Increase in Profits: {month_of_max} : (${max(diff)})')
    print(f'Greatest Decrease in Profits: {month_of_min} : (${min(diff)})') 
     