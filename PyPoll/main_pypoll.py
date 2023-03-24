# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import csv

file = "Resources/election_data.csv"

Unique_Candidates = {}
Total_Votes = 0 
Percentage_of_votes = []

with open(file, "r", encoding="utf-8") as csvhandler:
    csvreader = csv.reader(csvhandler,delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader: 
        Total_Votes += 1
        if row[2] not in Unique_Candidates:
            Unique_Candidates[row[2]] = 1   # put a name in the dictionary for each new candidate
        else:
            Unique_Candidates[row[2]] += 1  # count the votes for each candidate

    # for key,value in Unique_Candidates.items(): 
    #     Percentage_of_votes.append(round(((value/Total_Votes)*100),3))  # percentage of votes that each candidate won 

max_key = max(Unique_Candidates,key=Unique_Candidates.get) # tells us who won the most votes 


print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------")


for key,value in Unique_Candidates.items():
    print(f"{key}: {(round(((value/Total_Votes)*100), 3))}% ({value})")

print("-------------------------")
print(f"Winner: {max_key}")
print("-------------------------")


# print(max_key)

# print(Percentage_of_votes)

# print(Unique_Candidates)
    # for key,value in Unique_Candidates.items():
    #     print(f"{key} {value}")

textfile_path = "Analysis/PyPoll_Results_Text.txt"

with open(textfile_path, "w") as f: 
    f.write("Election Results")
    f.write("\n-------------------------")
    f.write(f"\nTotal Votes: {Total_Votes}")
    f.write("\n-------------------------")
    for key,value in Unique_Candidates.items():
        f.write(f"\n{key}: {(round(((value/Total_Votes)*100), 3))}% ({value})")
    f.write("\n-------------------------")
    f.write(f"\nWinner: {max_key}")
    f.write("\n-------------------------")
