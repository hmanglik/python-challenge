import os
import csv


csvpath =  os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join('analysis', 'results.txt')

# Set initial dictionary and counters 
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
        
        # If candidate not already in candidate_dict, add candidate and give them one vote
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1

        # If candidate already in candidate_dict, add one vote for the candidate
        else:
            candidate_dict[row[2]] += 1


# Loop through the key, value in candidate_dict and find the percentage of votes each candidate won
for key, value in candidate_dict.items():
    percentage = "{:.3%}".format(value/total_votes)
    # Find the winner of the election based on popular vote 
    if value > update_value:
        update_value = value
        winner = key

# Output
output=(
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"{key}", f":{percentage}", f"({value})"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n")

print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)