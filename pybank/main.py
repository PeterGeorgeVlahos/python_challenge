import os

import csv

# To the grader: "I missed the forrest through the trees" as I began working with the csv concept.
# As I started, I began working the problem from lists I created, not realizing I should have done the 
# the same calculations from the reader.  When I realize the flaw in my thinking, it was too late 
# to turn back.  I powered through many for loops and conditions. Helpful hints in the instrucstions
# had me thinking to take very small bites.  Second project much cleaner.  Good Luck with this one. 
# csvpath is variable  for pathway to file csv file

csvpath = os.path.join('Resources','budget_data.csv')

#create 3 list ->  Dates Revenue & change in rev.
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
        # here is where I started down the difficult path    
        dates.append(row[0])
        revenue.append(int(row[1]))

        row_counter = row_counter + 1

sum_net=()
sum_net_rev = 0
ave_month_difference = 0

# define function to sum of all elements in a list"
def sum_net (list):
    sum=0
    for i in list:
        sum += i
        return sum
    
sum_net_rev = sum_net(revenue)

# Once I found the total revenue, I needed the change in reveneu so I
# created another list with the net difference between months
for i in range(1,row_counter):
    change_in_revenue.append(revenue[i] - revenue[i-1])

#count number of rows in list change_in_revenue to find the average change
counter_change_in_revenue = 0
for a in (change_in_revenue):
    counter_change_in_revenue = counter_change_in_revenue +1

#run def function form change in range. Here I get to use my newly created function for a second time
sum_month_difference = sum_net(change_in_revenue)
ave_month_difference = round(float(sum_month_difference/counter_change_in_revenue),2)

#dates list with one less element to zip 2and create a way to find dates of min/max changes
dates.pop(0)
date_change_rev_list = [I for I in zip(dates, change_in_revenue)]

#Find the Larget Increase in Net Profits and then the corresponding date 
max_b = 0
min_c = 0

for x in range(1,84):
    if change_in_revenue[x] > max_b:
        max_b = (change_in_revenue[x])
        

    if change_in_revenue[x] < min_c:
        min_c = (change_in_revenue[x])


    
# for e in date_change_rev_list:
#     if e[1]==max_b:

# for c in range(1,84):
#     if change_in_revenue[c] < min_c:
#         
#     print(f"Greatest Decrease in Profits: $({min_c})")
    
# for x in date_change_rev_list:
#     if x[1]==min_c:
#         print(x[0])
#         print(x[1])
#         print(f"Min Value $ {min_c}")

print(f"Total Months: {row_counter}")
print(f"Total:  ${sum_net_rev}")
print(f"Average Charge: ${ave_month_difference}")
print(f"Greatest Increase in Profits: {(e[0])} (${(e[1])})")




output_file = os.path.join("new_date_rev.csv")

# with open(output_file, "w", newline='') as datafiles:
#     writer = csv.writer(datafiles)

#     # write a header row
#     writer.writerow(["Date","Revenue","Profit/Lose"])

#     writer.writerows(new_clean_file)