# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import csv

file = "Resources/budget_data.csv"

Number_of_months = []
Total_pl = []
ProfitLossDifferences = []

with open(file, "r", encoding="utf-8") as csvhandler:
    csvreader = csv.reader(csvhandler,delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        Number_of_months.append(row[0])
        Total_pl.append(int(row[1]))
    
    for i in range(1, len(Total_pl)): 
        ProfitLossDifferences.append(Total_pl[i] - Total_pl[i-1])

Profit_loss_average = round(sum(ProfitLossDifferences)/len(ProfitLossDifferences),2)  # this is our average change in P/L over entire period

Month_count = len(Number_of_months) # this is our answer for total number of months in the dataset (86)

Total_pl_sum = sum(Total_pl) # this is our answer for net total P/L over entire period 

profitloss_max = max(ProfitLossDifferences)
profitloss_min = min(ProfitLossDifferences)

max_inc_profit_month = Number_of_months[ProfitLossDifferences.index(profitloss_max) + 1]
max_dec_profit_month = Number_of_months[ProfitLossDifferences.index(profitloss_min) + 1]


pl_analysis = ("Financial Analysis" "\n------------------------"
               f"\nTotal Months: {Month_count}" f"\nTotal: ${Total_pl_sum}"
                 f"\nAverage Change: ${Profit_loss_average}"
                 f"\nGreatest Increase in Profits: {max_inc_profit_month} (${profitloss_max})"
                 f"\nGreatest Decrease in Profits: {max_dec_profit_month} (${profitloss_min})")

print(pl_analysis)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

textfile_path = "Analysis/PL_Analysis_Text.txt"

with open(textfile_path, "w") as f: 
    f.write(pl_analysis)
     
# print("------------------------")

# print("Financial Analysis")
# print("----------------------")
# print(f"Total Months: {Month_count}")
# print(f"Total: ${Total_pl_sum}")
# print(f"Average Change: ${Profit_loss_average}")
# print(f"Greatest Increase in Profits: {max_inc_profit_month} (${profitloss_max})")
# print(f"Greatest Decrease in Profits: {max_dec_profit_month} (${profitloss_min})")



# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


















    

