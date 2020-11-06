

import os
import csv



csvpath = os.path.join('budget_data.csv')


total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0


with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
    
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]
            
   
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]  
  
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)


    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print(average_change)
    print(greatest_inc_month, max(changes))
    print(greatest_dec_month, min(changes))


    PyBank = open("output.txt","w+")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' +"Total Months" + str(total_months)) 
    PyBank.write('\n' +"Total Amount" + str(total_revenue)) 
    PyBank.write('\n' +"Average" + str(average_change)) 
    PyBank.write('\n' +greatest_inc_month) 
    PyBank.write('\n' +str(high))
    PyBank.write('\n' +greatest_dec_month) 
    PyBank.write('\n' +str(low))  
