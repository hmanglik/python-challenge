import os
import csv


csvpath =  os.path.join('Resources', 'election_data.csv')

candidate_dict = {}
total_votes = 0
update_value = 0  

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')
    # Skip the header row
    csv_header = next(csvreader)

    # Get the total number of votes
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1
        else:
            candidate_dict[row[2]] += 1

# Output
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for key, value in candidate_dict.items():
    percentage = "{:.3%}".format(value/total_votes)
    print(key, f":{percentage}", f"({value})")
    if value > update_value:
        update_value = value
        winner = key
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
