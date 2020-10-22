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

    print("")
    print(f"Sum of Net Profit/Loss ${sum_net_rev}")
    print("")

    #create list of net difference between months
    for i in range(1,row_counter):
        change_in_revenue.append(revenue[i] - revenue[i-1])

    #count number of rows in list change_in_revenue
    count_a = 0
    for a in (change_in_revenue):
        count_a= count_a+1
    print(f"Number of row is change in revenue is {count_a} ")

    #run def function form change in range
    sum_month_difference = sum_net(change_in_revenue)
    ave_month_difference = round(float(sum_month_difference/count_a),2)
    print(f"Differnce in revenue each month ${ave_month_difference}")

    #Larget Increase in Net Profits
    max_b=0
    for b in range(1,84):
        if change_in_revenue[b] > max_b:
            max_b = (change_in_revenue[b])
    print(f"Max Value $ {max_b}")

    
    min_c=max_b
    for c in range(1,84):
        if change_in_revenue[c] < min_c:
            min_c = (change_in_revenue[c])
    print(f"Min Value $ {min_c}")

    #dates, change_in_revenue 




# zipped 2 list, create a variable to hold list
new_clean_file = zip(dates, revenue)

output_file = os.path.join("new_date_rev.csv")

with open(output_file, "w", newline='') as datafiles:
    writer = csv.writer(datafiles)

    # write a header row
    writer.writerow(["Date","Revenue","Profit/Lose"])

    writer.writerows(new_clean_file)