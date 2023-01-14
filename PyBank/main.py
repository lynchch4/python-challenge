import os
import csv

# print header
print("")
print("Financial analysis")
print("")
print("-----------------------------------------")
print("") 
 
# assign variables
count = 0
total = 0
max = 0
min = 0
previous = 0
change = 0
changetotal = 0
average = 0
count2 = 0

# set path for files
path_name = '/Users/Chris/OneDrive/Documents/python-challenge/PyBank/Resources'

csvpath = os.path.join("", "Resources", "budget_data.csv")

out_name = '/Users/Chris/OneDrive/Documents/python-challenge/PyBank/analysis'

out_path = os.path.join("", "analysis", "bank_analysis.txt")
    
# open CSV file as read
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header
    next(csvreader, None)

    # for loop
    for row in csvreader:

       # count of total months
       count += 1
       
       # sum of monthly investments
       total += int(row[1])

       # skip results where there was not previous change in profit/loss
       if previous == 0:
        change = 0
       elif previous != 0:
        change = int(row[1]) - previous
        count2 += 1

       # sum of change in variance
       changetotal += change 

       # assign variable for previous row profit/loss
       previous = int(row[1])
     
       # find min/max date and amount for change in profit/loss
       if int(change) > int(max):
        max = int(change)
        datemax = row[0]
       
       if int(change) < int(min):
        min = int(change)
        datemin = row[0]
    
    average = round(changetotal / (count2), 2)

    # print results
    print("Total Months: " + str(count))
    print("")
    print("Total: $" + str(total))
    print("")
    print("Average Change: $" + str(average))
    print("")
    print("Greatest Increase in Profits: " + str(datemax) + " ($" + str(max) + ")")
    print("")
    print("Greatest Decrease in Profits: " + str(datemin) + " ($" + str(min) + ")")
    print("")
 
# produce textfile for results
with open(out_path, 'w') as textfile:
    textfile.writelines(["\n", "Financial Analysis \n", "\n", "---------------------------------------------------- \n", "\n", "Total Months: " + str(count) + "\n",
    "\n", "Total: $" + str(total) + "\n", "\n", "Average Change: $" + str(average) + "\n", "\n", "Greatest Increase in Profits: " + str(datemax) + " ($" + str(max) + ")" + "\n", "\n",
    "Greatest Decrease in Profits: " + str(datemin) + " ($" + str(min) + ") \n"])