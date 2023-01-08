import os
import csv

# Header
print("")
print("Election Results")
print("")
print("--------------------------------")
print("")
    
# set path for files


csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath, encoding='utf') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

print(os.getcwd())

