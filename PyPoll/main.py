import os
import csv


# print header
print("")
print("Election Results")
print("")
print("--------------------------------")
print("")
    
# assign variables
total = 0
charles = 0
diana = 0
raymon = 0

# set path for files
path_name = '/Users/Chris/python-challenge/PyPoll/Resources'

csvpath = os.path.join("", "Resources", "election_data.csv")

out_name = '/Users/Chris/python-challenge/PyPoll/analysis'

out_path = os.path.join("", "analysis", "election_analysis.txt")

# open CSV file as read
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    next(csvreader, None)

    # for loop
    for row in csvreader:
        
        # add a counter
        total += 1

        # assign a counter for each candidates
        if row[2] == "Charles Casper Stockham":
            charles += 1
        elif row[2] == "Diana DeGette":
            diana += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon += 1

        # assign variables for percentage of votes and round to 3 decimals
        cper = round(charles/total*100, 3)
        dper = round(diana/total*100, 3)
        rper = round(raymon/total*100, 3)

        # if statement for which candidate had most votes
        if charles > diana and charles > raymon:
            winner = "Charles Casper Stockham"
        elif diana > charles and diana > raymon:
            winner = "Diana DeGette"
        elif raymon > diana and raymon > charles:
            winner = "Raymon Anthony Doane"
    
    # print results
    print("Total Votes: " + str(total))
    print("")
    print("--------------------------------")
    print("")
    print("Charles Casper Stockham: " + str(cper) + "% (" + str(charles) + ")")
    print("")
    print("Diana DeGette: " + str(dper) + "% (" + str(diana) + ")")
    print("")
    print("Raymon Anthony Doane: " + str(rper) + "% (" + str(raymon) + ")")
    print("")
    print("--------------------------------")
    print("")
    print("Winner: " + str(winner))
    print("")
    print("--------------------------------")

# produce textfile for results
with open(out_path, 'w') as textfile:
    textfile.writelines(["\n", "Election Results \n", "\n", "---------------------------------------------------- \n", "\n", "Total vote: " + str(total) + "\n",
    "\n", "---------------------------------------------------- \n", "\n", "Charles Casper Stockham: " + str(cper) + "% (" + str(charles) + ")" + "\n", "\n", 
    "Diana DeGette: " + str(dper) + "% (" + str(diana) + ")" + "\n", "\n", "Raymon Anthony Doane: " + str(rper) + "% (" + str(raymon) + ") \n", "\n", 
    "---------------------------------------------------- \n", "\n", "Winner: " + str(winner) + "\n", "\n" "---------------------------------------------------- \n"])