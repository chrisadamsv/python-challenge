# Import the os and csv modules into the script
import os
import csv

# Create a path to the csv file to be used
csvpath = os.path.join('Documents','August_Data_Analytics_Cohort','DataBootcamp','Homework-Repositories','python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

# Create a list to store the date values and the difference between the profits of each month
dates = []
profits_losses = []
# Create variables to hold the values to be calculated i.e. total profit, the value of the previous month, the difference between the two, and the total months
total_profit = 0
dollar_value = 0
difference = 0
months = 1

# Open up the csv file and skip the header and hold the first row of data in dollar_value, then add that to the total profit to start
with open(csvpath, 'r', newline='' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    dollar_value = int(first_row[1])
    total_profit += dollar_value

# Loop through all the rows after the header and first, store the dates in the list, calculate the difference between the two months, add the difference to the list...
# ... change the dollar_value to the current row, and the current row to the total, and add the row to the months variable
    for row in csvreader:
        dates.append(row[0])
        difference = (int(row[1]) - dollar_value) 
        profits_losses.append(difference)
        dollar_value = int(row[1])
        total_profit = (total_profit + dollar_value)
        months += 1

# Calculate the average value with the numbers in the "profits_losses" list
    average_difference = (sum(profits_losses)/len(profits_losses))

# Calculate the month with the largest increase in profits, then grab the index of that value to pull the month
    largest_increase = max(profits_losses)
    l_i_index = profits_losses.index(largest_increase)
    l_i_date = dates[l_i_index]

# Calculate the month with the largest decrease in profits, then grab the index of that value to pull the month
    largest_decrease = min(profits_losses)
    l_d_index = profits_losses.index(largest_decrease)
    l_d_date = dates[l_d_index]

# Print the results of the code below: 
print("-------------------------------------") 
print("Financial Analysis")
print("-------------------------------------") 
print(f"Total Months: {months}") 
print(f"Total: ${total_profit}")   
print(f"Average Change: ${str(round(average_difference, 2))}")
print(f"Greatest Increase In Profits: {l_i_date} (${largest_increase})")
print(f"Greatest Decrease In Profits: {l_d_date} (${largest_decrease})")
print("-------------------------------------") 

# Dictate a path where the .txt file will go
text_file_path = 'Documents/August_Data_Analytics_Cohort/DataBootcamp/Homework-Repositories/python-challenge/PyBank/Analysis/pybank.txt'

# Create the .txt file and write each individual 'print' line to the file.
with open(text_file_path, "w") as file:
    file.write("-------------------------------------\n")
    file.write("Financial Analysis\n")
    file.write("-------------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${total_profit}\n")   
    file.write(f"Average Change: ${str(round(average_difference, 2))}\n")
    file.write(f"Greatest Increase In Profits: {l_i_date} (${largest_increase})\n")
    file.write(f"Greatest Decrease In Profits: {l_d_date} (${largest_decrease})\n")
    file.write("-------------------------------------\n")