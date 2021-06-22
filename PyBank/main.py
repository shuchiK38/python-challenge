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
    month = [] #this List will be used to get the Date index value for #4 and #5 
    data = []  #this is the List of all profits and losses
    for row in csv_reader:
        
        if num_rows > 0:
            total = total + int(row[1])
            month.append (row[0])
            data.append (int(row[1]))

        num_rows += 1
    
    i = 0
    diff = [] #this List will store the difference of consecutive years for the entire period
    while i < len(data) - 1:
        diff.append (data[i+1] - data[i])
        i = i + 1

    sum = 0
    j = 0
    while j < len(diff): #iterating through diff List to get the sum of all profit/loss differences
        sum = sum + diff[j]
        j = j + 1

    average = '{:.2f}'.format( sum / len(diff) )

    index_of_max = diff.index(max(diff)) #index of maximum value in diff List
    index_of_min = diff.index(min(diff)) #index of minimum value in diff List

    month_of_max = month[index_of_max+1] #month List index is diff List index + 1, since diff List starts at +1
    month_of_min = month[index_of_min+1]

    #terminal output
    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {num_rows - 1}')
    print(f'Total:$ {total}')
    print(f'Average Change: {average}')
    print(f'Greatest Increase in Profits: {month_of_max} : (${max(diff)})')
    print(f'Greatest Decrease in Profits: {month_of_min} : (${min(diff)})') 
    
    #output in a text file
    with open('analysis/PyBank_Output.txt', 'w') as output:
        print(f'Financial Analysis', file=output)
        print(f'----------------------------', file=output)
        print(f'Total Months: {num_rows - 1}', file=output)
        print(f'Total:$ {total}', file=output)
        print(f'Average Change: {average}', file=output)
        print(f'Greatest Increase in Profits: {month_of_max} : (${max(diff)})', file=output)
        print(f'Greatest Decrease in Profits: {month_of_min} : (${min(diff)})', file=output)
