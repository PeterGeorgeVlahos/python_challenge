import os

import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    print(csvreader)

    #read the header row first (eliminate for counting)
    csv_header = next(csvreader)
    
    #set row counter to zero
    row_counter = 0
    sum_profit = 0
    for x in csvreader:


        #create tuple w/date:rev paired w/date string & rev interger
        date_rev_tuple= (str(x[0]),float(x[1]))
        
        #check tuple
        #print(date_rev_tuple) WORKS
        print(date_rev_tuple[1])


        row_counter +=1
        #difference between x & X-1 
        # append list
        #diff_rev_day = (date_rev_tuple([1]) - date_rev_tuple([1])-1))
        #print(date_rev_tuple(x[1])
        #print(diff_rev_day)
        #print(date_rev_tuple(x[1]))
    # row (-header) = total rows
    print(row_counter)