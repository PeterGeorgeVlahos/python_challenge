import os

import csv

# csvpath is variable  for pathway to file csv file
csvpath = os.path.join('Resources','budget_data.csv')

#create 2 list 1 for dates 2 for revenue
dates = []
revenue = []
change_in_revenue = []

# open with path variable, new line data 
with open(csvpath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    header=next(csvreader)
    row_counter=0

    for row in csvreader:
        #print(row)
        #import pdb; pdb.set_trace()
            
        dates.append(row[0])
        revenue.append(int(row[1]))

        row_counter = row_counter + 1
    print(row_counter)
    
    # define function to sum of all elements in a list
    def sum_net (list):
        sum=0
        for i in list:
            sum += i
        return sum

    # Define Total of Net Revenue equal to [rev list], 
    sum_net_rev = sum_net(revenue)

    #create a new list, net difference between months
    for i in range(2,row_counter):
        change_in_revenue.append = (revenue(i[0]) - revenue(i-1[0]))


    for j in change_in_revenue:
        print(change_in_revenue[j])
        


    print("")
    print(f"Sum of Net Profit/Loss ${sum_net_rev}")
    print("")
    




# zipped 2 list, create a variable to hold list
new_clean_file = zip(dates, revenue)

output_file = os.path.join("new_date_rev.csv")

with open(output_file, "w", newline='') as datafiles:
    writer = csv.writer(datafiles)

    # write a header row
    writer.writerow(["Date","Revenue","Profit/Lose"])

    writer.writerows(new_clean_file)