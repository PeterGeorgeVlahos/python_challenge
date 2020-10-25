import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

output_path = os.path.join('election_analysis.txt')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csvheader = next(csvreader)
    #print(csvheader)

    total_votes = 0
    
    can_1_votes = 0
    can_2_votes = 0
    can_3_votes = 0
    can_4_votes = 0
    can_unknown_votes = 0
    
    name_1_can = "Khan"
    name_2_can = "Correy"
    name_3_can = "Li"
    name_4_can = "O'Tooley"
    name_unknown_can = "unknown"
 

    for a in csvreader:
        total_votes = total_votes + 1

        # vote count per canidate
        if a[2] == name_1_can:
            can_1_votes += 1
        elif a[2]== name_2_can:
            can_2_votes += 1
        elif a[2] == name_3_can:
            can_3_votes += 1
        elif a[2] == name_4_can:
            can_4_votes = can_4_votes + 1
        else:
            can_unknown_votes = total_votes - (can_1_votes+can_2_votes+can_3_votes+can_4_votes)
            print(f"There are other canidates: {can_unknown_votes}")
    
        # find winner (next time build code win any number of canidates)
        if can_1_votes > can_2_votes and can_1_votes > can_3_votes  and can_1_votes > can_4_votes and can_1_votes > can_unknown_votes:
            winning_can = name_1_can
        elif can_2_votes > can_1_votes and can_2_votes > can_3_votes and can_2_votes > can_4_votes and can_2_votes > can_unknown_votes:
            winning_can = name_2_can
        elif can_3_votes > can_1_votes and can_3_votes > can_2_votes and can_3_votes > can_4_votes and can_3_votes > can_unknown_votes:
            winning_can > name_3_can
        elif can_4_votes > can_1_votes and can_4_votes > can_2_votes and can_4_votes > can_3_votes and can_4_votes > can_unknown_votes:
            winning_can > name_4_can
        elif can_unknown_votes > can_1_votes and can_unknown_votes > can_2_votes and can_unknown_votes > can_3_votes and can_unknown_votes > can_4_votes:
            winning_can = can_unknown_votes
        else:
            winning_can = "Unknown Canidate Won"

    
    # Percenatge of votes
    percentage_of_can_1_votes = round(can_1_votes/total_votes*100)
    percentage_of_can_2_votes = round(can_2_votes/total_votes*100)
    percentage_of_can_3_votes = round(can_3_votes/total_votes*100)
    percentage_of_can_4_votes = round(can_4_votes/total_votes*100)
    percentage_of_can_unknown_votes = round(can_unknown_votes/total_votes*100)



output = (
    "Election Results\n"
    "---------------------------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    "---------------------------------------------------------\n"
    f"{name_1_can}:  {percentage_of_can_1_votes}.000% ({can_1_votes})\n" 
    f"{name_2_can}:  {percentage_of_can_2_votes}.000% ({can_2_votes})\n"
    f"{name_3_can}:  {percentage_of_can_3_votes}.000% ({can_3_votes})\n"
    f"{name_4_can}:  {percentage_of_can_4_votes}.000% ({can_4_votes})\n"
    "---------------------------------------------------------\n"
    f"The winning canidate is {winning_can}"
)


#Winner is


with open('election_analysis.txt', 'w') as txt_file:
    txt_file.write(output)



    



