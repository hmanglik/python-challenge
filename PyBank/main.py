import os
import csv

csvpath =  os.path.join('Resources', 'budget_data.csv')
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

    for c, value in enumerate(changes):
        if value > greatest_increase:
            greatest_increase = value
            greatest_month = dates[c+1]
        if value < greatest_decrease:
            greatest_decrease = value
            lowest_month = dates[c+1]


# Output
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: $ {counter}")
print(f"Average Change: {avg_change}") 
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})")