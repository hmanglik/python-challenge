import os
import csv

# Get the relative path
csvpath =  os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join('analysis', 'results.txt')

# Define empty lists and counters
dates = []
profit_losses = []
changes = [] 
counter = 0
greatest_increase = 0
greatest_decrease = 0 

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')

    # Skip the header row
    csv_header = next(csvreader)

    # Read each row of data after the header and append to two lists. Use a counter to get the net total amount of "Profit/Losses" over the entire period 
    for row in csvreader:
        dates.append(row[0])
        profit_losses.append(int(row[1]))
        counter += int(row[1])
    # Get the total number of months included in the dataset
    total_months = len(dates)
    
    # Loop through the indices of profit_losses to get the average of the changes in "Profits/Losses" over the entire period
    for i in range(1, len(profit_losses)):
        diff = profit_losses[i] - profit_losses[i-1]
        changes.append(diff)
    total = sum(changes)
    avg_change = round(total/(len(profit_losses)-1), 2)

    # Loop through the changes list using enumerate method
    for c, value in enumerate(changes):
        # Get the greatest increase in profits and the corresponding month
        if value > greatest_increase:
            greatest_increase = value
            greatest_month = dates[c+1]
        # Get the greatest decrease in profits and the corresponding month
        if value < greatest_decrease:
            greatest_decrease = value
            lowest_month = dates[c+1]


# Output
output=(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${counter}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})\n")

print (output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

