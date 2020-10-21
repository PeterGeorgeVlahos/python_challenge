import os

import csv

# csvpath is variable  for pathway to file csv file
csvpath = os.path.join('Resources','budget_data.csv')

#create 2 list 1 for dates 2 for revenue
dates = []
revenue = []
profit_loss = []
net_sum_p_l = 0

# open with path variable, new line data 
with open(csvpath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    header=next(csvreader)
    row_counter=0

    for row in csvreader:
        #print(row)
        #import pdb; pdb.set_trace()
            
        dates.append(row[0])
        revenue.append(float(row[1]))

        row_counter = row_counter + 1
    print(row_counter)

    
    for j in range(2,row_counter):

        # net sum p/l

        # Difference between rev j & rev j-1
        profit_loss = (revenue[j] - revenue[j-1])
        #print(profit_loss)

        #


# zipped 2 list, create a variable to hold list
new_clean_file = zip(dates, revenue)

output_file = os.path.join("new_date_rev.csv")

with open(output_file, "w", newline='') as datafiles:
    writer = csv.writer(datafiles)

    # write a header row
    writer.writerow(["Date","Revenue"])

    writer.writerows(new_clean_file)