# Election Analysis

# Project Overview
The Colorado Board of Elections employees Seth and Tom requested an election audit of a recent local congressional election. For the analysis we were tasked with the following:

- Calculate the total number of votes cast. 
- Get a complete list of candidates who received votes. 
- Calculate the total number of votes each candidate received. 
- Calculate the percentage of votes each candidate won.
- Determine the winner of the election based on popular vote.

The election commission was pleased with our analysis and requested additional data to complete the audit. We set out to find the following additional information about the counties who participated in the election: 
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest voter turnout 

# Adjusting Our Code 
We started by using our existing code and added additional variables for the county data. Given that we were doing the same type of analysis as we did with candidates we simply duplicated the methods we used in the original code. The csv file we used for the original analysis included the county data so we did not need any additional resources. 

## Step 1: Create County Variables
Our first task was to create a list and dictionary for the counties. We also needed to delcare variables to track and calculate the vote count for each county. 

![Candidate and County lists and dictionaries](https://user-images.githubusercontent.com/66224990/166068736-2c787f27-bf50-4336-a7c8-94bee4ab98f4.png)

## Step: 2 Track County Votes
![If county not in list or dictionary](https://user-images.githubusercontent.com/66224990/166069260-f264ce23-f5a7-491a-8a60-ca9ec455095b.png)


## Step 3: Loop Through Data & Print Results
![For loop and print statements](https://user-images.githubusercontent.com/66224990/166069263-6d8933f9-44e9-4f51-b52c-bc96a3abc511.png)

# Election Results
The analysis of the election showed that:
- There were 369,771 votes cast in the election. 
- There were 3 counties that had voter turnout: 
	- Jefferson
	- Denver 
	- Arapahoe
- The county vote percentages and total votes were:
	- Jefferson: 10.5% (38,855)
	- Denver: 82.8% (306,055)
	- Arapahoe: 6.7% (24,801)
- The county with highest voter turnout was: Denver
- The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
    - Diana DeGette received 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
- The winner of the election was: 
    - Diana Degette, who received 73.8% of the vote and 272,892 votes

Our code included formatting with dashes and new lines that resulted in the following being printed to the terminal and a text file. 

## Terminal Print
![Terminal results](https://user-images.githubusercontent.com/66224990/166069124-5404da2c-8ff7-425c-99ff-6733ad77a753.png)


## Text File Print
![Text file results](https://user-images.githubusercontent.com/66224990/166069154-4c01c12b-9937-4255-9b3a-867f10c2cbd9.png)

# Challenge Summary
Our analysis was for a congressional seat for state of Colorado, which had 3 candidates and 3 counties in the district. The script we used to find the candidate and to find the county analysis was identical, therefore we could change the candidate and county variables to complete an analysis for any type of election. 
## Change the administrative district
We could change the county variable to any other type of population sector, for example: city, province, state, country, etc. 
## Change the voter choices
We could change the candidate variable to another list of options being voted on, for example: propositions, measures, bills, etc.

