# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("\\Users\\Propietario\\Desktop\\git\\tdm-mon-data-pt-07-2020-u-c\\Homework 3\\PyBank\\Resources\\budget_data.csv")
#print (csvpath)
#In addition, your final script should both print the analysis to the terminal and export a text file.
output_txt = os.path.join("\\Users\\Propietario\\Desktop\\git\\tdm-mon-data-pt-07-2020-u-c\\Homework 3\\PyBank\\Resources\\output.txt")

number_of_months = 0
net_total = 0
dif = 0
ginc = 0 
gdec = 0 
prevalue = 0
diftotal = 0
profit_losses = []
average = 0


print("----------------------------------------------")


print("Financial Analysis")
print("----------------------------------------------")

# Open the CSV and read the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for x in csvreader:

        month = x[0]
        Amount =x[1]  

        #Total number of months
        number_of_months = number_of_months + 1
        #Net total amount of Pofit/Losses over the entire period
        net_total += int(Amount)
        #Generate a new list
        profit_losses.append(x)
        

    for i in range(1, number_of_months, 1):

        diff = int(profit_losses[i][1]) - int(profit_losses[i-1][1])
        diftotal = diftotal + diff     
        #Greatest increase in profits (financial analysis)
        if ginc < diff:
            ginc = diff
            gincdate = profit_losses[i][0]
         #Greatest decrease in profits (financial analysis)
        if gdec > diff:
            gdec = diff
            gdecdate = profit_losses[i][0]

    #Average of the changes in "Profit/Losses"
    average = diftotal / (number_of_months - 1)

print (f"The total number of months is: {number_of_months}")
print (f"The net total amount is: {net_total}")
print (f"The average of the changes is: {average}")
# Greatest increase in profit
print(f'Greatest Increase in Profits: {gincdate} : ($ {ginc})')
# Greatest increase in profit
print(f'Greatest Decrease in Losses: {gdecdate} : ($ {gdec})')

#In addition, your final script should both print the analysis to the terminal and export a text file.
# write to text file       
text_file = open(output_txt, "w")
text_file.write("----------------------------------------------")
text_file.write("\nFinancial Analysis")
text_file.write("\n----------------------------------------------")
text_file.write(f"\nThe total number of months is: {number_of_months}")
text_file.write(f"\nThe net total amount is: {net_total}")
text_file.write(f"\nThe average of the changes is: {average}")
text_file.write(f'\nGreatest Increase in Profits: {gincdate} : ($ {ginc})')
text_file.write(f'\nGreatest Decrease in Losses: {gdecdate} : ($ {gdec})')
text_file.close()
