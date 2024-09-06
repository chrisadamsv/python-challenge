# Import the os and csv modules into the script
import os
import csv

# Create a path to the csv file to be used
csvpath = os.path.join('Documents','August_Data_Analytics_Cohort','DataBootcamp','Homework-Repositories','python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Create a variable to tabulate the total votes cast
total_votes = 0
# Create a list to store the candidate names, their vote share, and the percentage they share
candidates = []
vote_share = []
percent_share = []

# Open up the csv file and skip the header
with open(csvpath, 'r', newline='' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
# Loop through each row after the header and tabulate each row into the total_votes, then...
    for vote in csvreader:
        total_votes += 1
# ... check if the candidate does NOT exist in the candidates list. If they do not, add their name to the candidate list and add the vote to their vote share
        if vote[2] not in candidates:
            candidates.append(vote[2])
            vote_share.append(1)
# If they are on the candidates list, pull their name in the index and add the vote to their vote share
        else:
            candidates_index = candidates.index(vote[2])
            vote_share[candidates_index] += 1

# Loop through the list of candidates and calculate their share of the vote against the total votes recieved, then format to a percent and add that number to the percent_share list   
    for i in range(len(candidates)):
        percentage = (int(vote_share[i])/total_votes)
        formatted_percentage = f"{percentage:.3%}"
        percent_share.append(formatted_percentage)

# Calculate the winner by finding who has the largest vote_share, then use the index to find their name
    winner = max(vote_share)
    winner_index = vote_share.index(winner)
    winner_name = candidates[winner_index]

# Print the results of the code below: 
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
# Loop through the candidates to print their name, percentage, and vote share
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_share[i]} ({vote_share[i]})")
print("----------------------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Dictate a path where the .txt file will go
txt_file_path = 'Documents/August_Data_Analytics_Cohort/DataBootcamp/Homework-Repositories/python-challenge/PyPoll/Analysis/pypoll.txt'

# Create the .txt file and loop though the 'lines' list to export each line to a .txt file.
with open(txt_file_path, "w") as file:
    file.write("-------------------------\n")
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------------------\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {percent_share[i]} ({vote_share[i]})" + "\n")
    file.write("----------------------------------------\n")
    file.write(f"Winner: {winner_name}\n")
    file.write("-------------------------\n")