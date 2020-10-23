import os

import csv

# csvpath is variable  for pathway to file csv file
csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join('analysis.txt')

#create 2 list 1 for dates 2 for revenue
dates = []
total_months = 0
total_net = 0
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue = []
change_in_revenue = []

# open with path variable, new line data 
with open(csvpath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    header=next(csvreader)
    # row_counter=0

    first_row = next(csvreader)
    total_months += 1
    # row_counter += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        #print(row)
        #import pdb; pdb.set_trace()
        total_months += 1
        total_net += int(first_row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = int(row[1])
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = int(row[1])

        dates.append(row[0])
        revenue.append(int(row[1]))
        # row_counter = row_counter + 1

print(len([]))
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# print(f"Total Months: {row_counter}")

output = (
    f"Total Months: {total_months}\n"
    f"Average Change: {net_monthly_avg}\n"
)

print(output)

with open('analysis.txt', 'w') as txt_file:
    txt_file.write(output)
    
#     # define function to sum of all elements in a list
#     def sum_net (list):
#         sum=0
#         for i in list:
#             sum += i
#         return sum

#     # Define Total of Net Revenue equal to [rev list], 
#     sum_net_rev = sum_net(revenue)

    
#     print(f"Total:  ${sum_net_rev}")
    

#     #create list of net difference between months
#     for i in range(1,row_counter):
#         change_in_revenue.append(revenue[i] - revenue[i-1])

#     #count number of rows in list change_in_revenue
#     count_a = 0
#     for a in (change_in_revenue):
#         count_a= count_a+1
    

#     #run def function form change in range
#     sum_month_difference = sum_net(change_in_revenue)
#     ave_month_difference = round(float(sum_month_difference/count_a),2)
#     print(f"Average Charge: ${ave_month_difference}")
    

#     #dates list with one less element  
#     # how many rows in date list
#     dates.pop(0)
#     count_k = 0
#     for z in (dates):
#         count_k = count_k + 1
#     print(f"ther are {k} row in Date List")




#     # zipped 2 list, create a variable to hold list
#     new_clean_file = zip(dates, change_in_revenue)
    
#     #Larget Increase in Net Profits
#     max_b=0
#     for b in range(1,84):
#         if change_in_revenue[b] > max_b:
#             max_b = (change_in_revenue[b])
#         #print(dates[b])
    
#     for e in new_clean_file:
#         if e[1]==max_b:
#             print(f"Greatest Increase in Profits: {(e[0])} (${(e[1])})")

#     min_c=0
#     for c in range(1,84):
#         if change_in_revenue[c] < min_c:
#             min_c = (change_in_revenue[c])
#     print(min_c)
    
#     for g in new_clean_file:
#         print(g)
            


# output_file = os.path.join("new_date_rev.csv")

# with open(output_file, "w", newline='') as datafiles:
#     writer = csv.writer(datafiles)

#     # write a header row
#     writer.writerow(["Date","Revenue","Profit/Lose"])

#     writer.writerows(new_clean_file)