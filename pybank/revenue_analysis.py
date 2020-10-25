import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join('financial_analysis.txt')

date_list =[]
revenue_list = []
change_in_revenue_list = []


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header=next(csvreader)

    total_revenue_months = 0
    total_sum_revenue = 0
    total_change_in_revenue = 0
    average_change_in_revenue = 0
   
    for row in csvreader:

        total_revenue_months += 1

        #lists created from csv reader

        date_list.append(row[0])
        revenue_list.append(int(row[1]))

#Creat function to find sums in lists (FIX need to figure out how to use a loop)
def sum_list (list):
    sum = 0
    for i in list:
        sum += i
    return sum

# Total revenue using def sum_list function
total_sum_revenue = sum_list(revenue_list)

# Change in monthly revenue list  
for i in range(1,total_revenue_months):
    change_in_revenue_list.append(revenue_list[i] - revenue_list[i-1])

#total change in revenue to find average change
total_change_in_revenue = sum_list(change_in_revenue_list)

#average change in rev using def function
average_change_in_revenue = round(total_change_in_revenue / (total_revenue_months-1),2)

#pop 1st row to zip equal elements in date/change rev list
date_list.pop(0)
date_change_rev_list = [I for I in zip(date_list, change_in_revenue_list)]

max = 0
min = 0
max_date = ''
min_date = ''
for x in date_change_rev_list:
    if x[1] > max:
        max = x[1]
        max_date = x[0]


for x in date_change_rev_list:
    if x[1] < min:
        min = x[1]
        min_date = x[0]


output = (
    'Financial Analysis\n'
    '--------------------------\n'
    f'Total Months: {total_revenue_months}\n'
    f'Total: {total_sum_revenue}\n'
    f'Average Change: {average_change_in_revenue}\n'
    f'Greatest Increase in Profits: {max_date} $({max})\n'
    f'Greatest Decrease in Profits: {min_date} $({min})\n'

)


with open('financial_analysis.txt', 'w') as txt_file:
    txt_file.write(output)
      
