import os
import csv

election_data = os.path.join("..","Python-challenge","PyPoll","Resources","election_data.csv")
#csvpath = os.path.join("\\Users\\Propietario\\Desktop\\TASKS_SGL\\Python\\Python-challenge\\PyPoll\\Resources\\election_data.csv")
#In addition, your final script should both print the analysis to the terminal and export a text file.
output_txt = os.path.join("..","Python-challenge","PyPoll","Resources","output.txt")

# Defining lists and initiate the counter of the total votes
candidates = []
numbervotes = []
percentagev = []
totalvotes = 0

# Open the CSV and read the CSV
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for x in csvreader: 
        #Total number of votes
        totalvotes += 1 

#If the candidate is not in the list, then add the new name in the new list with his/her vote, if not just sum..
#..the vote to the same name.
        if x[2] not in candidates:
            #Generate the new list
            candidates.append(x[2])
            index = candidates.index(x[2])
            numbervotes.append(1)
        else:
            index = candidates.index(x[2])
            numbervotes[index] += 1
    
    # Add to percentagev list 
    for y in numbervotes:
        percentage = (y/totalvotes) * 100
        percentage = "%.3f%%" % percentage
        #Generate a new list
        percentagev.append(percentage)
    
    # Find the winning candidate
    winner = max(numbervotes)
    index = numbervotes.index(winner)
    wincandidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalvotes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentagev[i])} ({str(numbervotes[i])})")
print("--------------------------")
print(f"Winner: {wincandidate}")
print("--------------------------")


#In addition, your final script should both print the analysis to the terminal and export a text file.
# write to text file

text_file = open(output_txt, "w")
text_file.write("--------------------------")
text_file.write("\nElection Results")
text_file.write("\n--------------------------")
text_file.write(f"\nTotal Votes: {str(totalvotes)}")
text_file.write("\n--------------------------")
for i in range(len(candidates)):
    text_file.write(f"\n {candidates[i]}: {str(percentagev[i])} ({str(numbervotes[i])})")
text_file.write("\n--------------------------")
text_file.write(f"\nWinner: {wincandidate}")
text_file.write("\n--------------------------")
text_file.close()
