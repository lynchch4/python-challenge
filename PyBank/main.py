import os
import csv

# Header
print("")
print("Financial analysis")
print("")
print("-----------------------------------------")
print("") 

    
# set path for files


csvpath = os.path.join("..", "Resources", "budget_data.csv")


with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")