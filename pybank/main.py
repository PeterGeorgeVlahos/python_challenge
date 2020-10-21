import os

import csv

# csvpath is variable  for pathway to file csv file
csvpath = os.path.join('Resources','budget_data.csv')

#create 2 list 1 for dates 2 for revenue
dates = []
revenue = []

# open with path variable, new line data 
with open(csvpath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    for row in csvreader:

        dates.append(row[1])

        revenue.append(float(row[2])

# zipped 2 list, create a variable to hold list
new_clean_file = zip(dates, revenue)

output_file = os.path.join("new_date_rev.csv")