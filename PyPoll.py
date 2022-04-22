# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

# Assign a variable for the file to load and the path.

file_to_load = 'election_results.csv'
election_data = open(file_to_load, 'r')

# To do: perform analysis

# Close the file

election_data.close()


