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
    candidate = []
    all_votes = []

    for row in csv_reader:
        if num_rows > 0:
            all_votes.append(row[2])
            if row[2] not in candidate:
                candidate.append(row[2])

        num_rows += 1
    
    #from collections import Counter
    counter = collections.Counter (all_votes)

    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {num_rows - 1}')
    print(f'-------------------------')    
    print(f'Candidates: {candidate}')
    print(f'all votes: {len(all_votes)}')
    print(f'all candidate: {len(candidate)}')
    print(f'Counter: {counter}')

    for person in counter:
        key = person
        value = counter[key]
        percent = int(value) / len(all_votes)
        print(f'{key}: {percent} ({value})')