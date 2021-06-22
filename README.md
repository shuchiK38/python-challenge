# python-challenge

This repository is for python programs.

#PyBank program

In this program based off of given financial records of a company, need to analyse below;
1. The total number of months included in the dataset
    This is accomplished by a simple for loop
2. The net total amount of "Profit/Losses" over the entire period
    CSV file has 2 columns - Date and Profit/Losses. Read the CSV file using csv.reader and store the data from each colum into a List. Using Profit/Losses List, the sum of all values is calculated
3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    To calculated the difference between 2 consecutive months data, iterate over Profit/Losses list and append each difference value in a separate diff List. This List then be used to calculate the average difference over the entire period. 
4. The greatest increase in profits (date and amount) over the entire period
    Using max() function get the index of maximum difference from the diff List, then this index from diff List is used to get the index value from the Date List create in #2, to get the corresponding month value
5. The greatest decrease in profits (date and amount) over the entire period
    Using min() function get the index of minimum difference from the diff List, then this index from diff List is used to get the index value from the Date List create in #2, to get the corresponding month value

#PyPoll program

In this program election data is provided and below needs to be evaluated;

1. The total number of votes cast
    This could have been accomplished by using something like below;
        num_rows = sum(1 for row in pollFile)
    but since we need to read each line, for loop is used to get the count.
    In this step I also created a list of Candidate column, which will be use to create the Counter collection
2. A complete list of candidates who received votes
    This is accomplished using Counter collection, and iterating over the Counter
3. The percentage of votes each candidate won
    Again using Counter, key/value was extracted for each candidates votes and % was calculated using total votes calculated in #1
4. The total number of votes each candidate won
    Same concpet as in #3
5. The winner of the election based on popular vote
    For this Counter.most_common() method is used and key is extracted from it, to show the Winner
