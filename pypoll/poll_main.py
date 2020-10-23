import os
import csv

csvpath = os.path.join('Resources','election_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csvheader = next(csvreader)
    print(csvheader)

    total_votes = 0
    candidate = []
    percent_vote = []
    votes_cast_for = []

    #3 column list No header [Name(0), Pect Total (1), Votes for(2) ]
    for a in csvreader:
        total_votes = total_votes + 1

        #do I want 1 list with per canidate OR 1 list per Object? Right 
        #now just find the the votes per canidate
        if csvreader[2] == "":


    



