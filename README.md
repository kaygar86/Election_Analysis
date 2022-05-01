# Election Analysis

# Project Overview
Colorado Board of Elections employees Seth and Tom requested an election audit of a recent local congressional election. For the analysis we were tasked with the following:

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
We started by using our existing candidate analysis code and added additional variables for the county data. Given that we were doing the same type of analysis as we did with candidates we simply duplicated the methods we used in the original code. The csv file we used for the original analysis included the county data so we did not need any additional resources. 

## Step 1: Create Variables
Our first task was to create a list and dictionary for the counties. We also needed to delcare variables to track and calculate the vote count for each county. 

![Candidate and County lists and dictionaries](https://user-images.githubusercontent.com/66224990/166068736-2c787f27-bf50-4336-a7c8-94bee4ab98f4.png)

## Step: 2 Track Votes
Next we created another If Statement within the first For Loop to track the number of times a county name appeared in the voter data. 
![If county not in list or dictionary](https://user-images.githubusercontent.com/66224990/166069260-f264ce23-f5a7-491a-8a60-ca9ec455095b.png)

We extracted this data from the second column in the csv, which had the county names. 
![For Loop County List](https://user-images.githubusercontent.com/66224990/166075646-05f29bab-165b-48fa-a1b1-f62ba2c07703.png)

![CSV](https://user-images.githubusercontent.com/66224990/166075508-a0683dd3-a224-4a70-9eb5-39adf42ea316.png)

## Step 3: Calculate Totals & Percentages
We created another For Loop to get the county from the dictionary we created. It calculated the number of votes for each county and the percentage each county got out of the total votes. The If Statement determined which county had the highest voter turnout.

![For loop and print statements](https://user-images.githubusercontent.com/66224990/166069263-6d8933f9-44e9-4f51-b52c-bc96a3abc511.png)

# Election Results
When we ran the code we got the following results:
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

## Print Formatted Results
Our final task was to print the results formatted with dashes and new lines to make it easy to read. The code formatting resulted in the following being printed to the terminal and written to a text file election_analysis.txt.

## Terminal Output
![Terminal results](https://user-images.githubusercontent.com/66224990/166069124-5404da2c-8ff7-425c-99ff-6733ad77a753.png)


## Text File Output
![Text file results](https://user-images.githubusercontent.com/66224990/166069154-4c01c12b-9937-4255-9b3a-867f10c2cbd9.png)

# Challenge Summary
Our analysis was for a congressional seat election for state of Colorado, which had 3 candidates that voters from 3 counties. The script we used to find the winning candidate and the largest voting county was identical, therefore we could change the variables and the f string results text to complete an analysis for any type of election. Here are the ways we could modify the code to suit a different election: 

Change the administrative district: We could change the county variable to any other type of population sector (examples: city, state, country, etc.). This would not require any change to how the largest voting sector is determined. 

Change the voter choices: We could change the candidate variable to another list of options being voted on (examples: propositions, measures, etc.). The data for an election of proposition or measure may be presented differently from that of a candidate, with a Yes or No indicating the winner instead of a multiple choice, so we may also have to tweak how the winning choice is determined. 

These modificationss would require us to also alter the variables and results printout text for each election, which may become cumbersome, but they would allow us to work with different types of data that may not match the one we used in this analysis. 

If we assume we would be working with candidate election data organized in the same way as the csv file we worked with (0 = ballot number, 1 = popultaion sector, 2 = candidate name) then we could write code with the more generic variables being pulled from the csv and then adjust the results f string so that it pulls the header of the csv file we're working with (candidate, county, state, etc). We would just need to make another variable for the header line that would replace where we currently refer to the county. 

