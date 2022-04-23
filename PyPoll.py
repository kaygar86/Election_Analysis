# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

# Assign a variable for the file to load and the path.
import csv
import os


file_to_load = os.path.join("Resources", "election_results.csv")



file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file. 
with open(file_to_load) as election_data:


# Read the file object with the reader function.

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)




