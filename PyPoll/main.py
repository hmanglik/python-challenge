import os
import csv

# Get the relative paths
csvpath =  os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join('analysis', 'results.txt')

# Set initial dictionary and counters 
candidate_dict = {}
total_votes = 0
pop_vote = 0  

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

# Export the results to text file and print the results
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Election Results\n")
    print(f"Election Results\n")
    txt_file.write(f"----------------------------\n")
    print(f"----------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    print(f"Total Votes: {total_votes}\n")
    txt_file.write(f"----------------------------\n")
    print(f"----------------------------\n")
    # Loop through the key, value in candidate_dict and find the percentage of votes each candidate won
    for key, value in candidate_dict.items(): 
        percentage = "{:.3%}".format(value/total_votes) 
        txt_file.write(f"{key}: {percentage} ({value})\n")
        print(f"{key}: {percentage} ({value})\n")
        # Find the winner of the election based on popular vote
        if value > pop_vote:
            pop_vote = value
            winner = key
    txt_file.write(f"----------------------------\n")
    print(f"----------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    print(f"Winner: {winner}\n")
    txt_file.write(f"----------------------------\n")
    print(f"----------------------------\n")

