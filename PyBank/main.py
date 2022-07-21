
# import dependencies
import os
import csv

# files to load and output
budget_load = os.path.join("Resources", "budget_data.csv")
budget_output = os.path.join("analysis", "budget_analysis.txt")

#set global variables
total_months = 0
net_total = 0
net_change_list = []
month_of_change = []
greatest_increase = ["",0]
greatest_decrease = ["", 999999999999999]

# Open and read csv
with open(budget_load) as buget_data:
    reader = csv.reader(buget_data)



 # Read header   
    header = next(reader)
    

  # Read first row     
    first_row = next(reader)
  
    #add to variables
    total_months +=1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])

#creat for loop

    for row in reader:

    #total months
     total_months += 1   
    # net total amount
     net_total += int(row[1])        

    # track change per month
     net_change = int(row[1]) - prev_net
     prev_net =  int(row[1])  
     net_change_list.append(net_change)
     
    
    # calculate average change 
     net_avg_change = sum(net_change_list) / len(net_change_list)

   
   #calculate greatest increase
     if net_change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = net_change

    #calculate greatest increase
     if net_change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = net_change


    
#-------------------------------------
    # print column (price)
price = int(row[1])

#---------------------------

#create summary

summary = (
        f"Financial Analysis\n"
        f"----------------------\n"
        f"Total Months: {int(total_months)}\n"
        f"Total: ${(net_total)}\n"
        f"Average Change: ${net_avg_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${(greatest_increase[1])})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${(greatest_decrease[1])})\n")

print(summary)

# print the analysis to the terminal

with open(budget_output, "w") as txt_file:
    txt_file.write(summary)
