# import dependencies

import os
import csv


#path for files to load and output

election_load = os.path.join("Resources", "election_data.csv")
election_output = os.path.join("analysis", "election_analysis.txt")


#set global variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0




# open file

with open(election_load) as csv_file:
    reader = csv.reader(csv_file)

    #read header
    header = next(reader)


    # create loop
    for row in reader:
        
        # add to total votes 
        total_votes += 1

        # get candidate name from each row
        candidate_name = row[2]

        # add vote per candidate
        if candidate_name not in candidate_options:

            # add to list of candidates
            candidate_options.append(candidate_name)

            

            # track candidate votes count
            candidate_votes[candidate_name] = 0

        #add vote for each candidates count

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
# Print the results and export the data to our text file
with open(election_output, "w") as txt_file:

        # Print the final vote count (to terminal)
    election_results = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)
    


        
        # loop through candidates

    for candidate in candidate_votes:

            #get vote count and the percentage

            vote_count = candidate_votes.get(candidate) 


            vote_percentage = (vote_count / total_votes) * 100
            
            
            # determine winner and count

            if (vote_count > winning_count):
                winning_count = vote_count
                winning_candidate = candidate
            
            voter_output = f"{candidate}: {vote_percentage:.3f}% ({vote_count})\n"

            print(voter_output)
            txt_file.write(voter_output)
           
    winner_results = (    
        f"------------------------\n"
        f"Winnner: {winning_candidate}\n"
        f"------------------------\n"
        )
            
    print(winner_results)

    txt_file.write(winner_results)

    


           
        



    



    
