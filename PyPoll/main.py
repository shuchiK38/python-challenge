import os
import csv
import collections

election_data = os.path.join ( 'Resources', 'election_data.csv')

# Tasks;
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

with open(election_data) as pollFile:
    csv_reader = csv.reader (pollFile, delimiter=',')
    num_rows = 0
    all_votes = [] #this List will store all the values in Candidate column for further calculations using Collections Counter

    for row in csv_reader:
        if num_rows > 0:
            all_votes.append(row[2])

        num_rows += 1
    
    counter = collections.Counter (all_votes) #initializing Counter 

    #for terminal output
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {num_rows - 1}')
    print(f'-------------------------')

    #for output in a text file
    with open('analysis/PyPoll_Output.txt', 'w') as output:
        print(f'Election Results', file=output)
        print(f'-------------------------', file=output)
        print(f'Total Votes: {num_rows - 1}', file=output)
        print(f'-------------------------', file=output)

        #iterating through counter to calculate % and total vote coutns for each candidate
        for person in counter:
            key = person
            value = counter[key]
            percent = '{:.3f}'.format( (int(value) / len(all_votes)) * 100 )
            print(f'{key}: {percent}% ({value})')
            print(f'{key}: {percent}% ({value})', file=output)

        print(f'-------------------------')
        #find out who is the Winner
        winner = counter.most_common(1)[0][0] if counter else None
        print(f'Winner: {winner}')
        print(f'-------------------------')

        print(f'-------------------------', file=output)
        print(f'Winner: {winner}', file=output)
        print(f'-------------------------', file=output)    