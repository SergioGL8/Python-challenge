# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("\\Users\\Propietario\\Desktop\\git\\tdm-mon-data-pt-07-2020-u-c\\Homework 3\\PyBank\\Resources\\budget_data.csv")
#print (csvpath)

number_of_months = 0
net_total = 0
print("----------------------------------------------")


print("Financial Analysis")
print("----------------------------------------------")

# Open the CSV and read the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for x in csvreader:

        #Total number of months
        number_of_months = number_of_months + 1
        #Net total amount of Pofit/Losses over the entire period
        net_total += int(x[1])
        

print (f"The total number of months is: {number_of_months}")
print (f"The net total amount is: {net_total}")



    






