import csv
#open path
csv_file = "Python---challenge\PyPoll\Resources\election_data.csv"
#define variables
totalballots = 0
candidateballots = []
ballots = 0
#open data csv  
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    print(header) 
    for row in csv_reader:
        print(row) 
        #retrieve nominee name from the row
        candidate = row[2]
    #add the candidate ballot counts
        if candidate not in candidateballots:
                candidateballots[candidate] = 1
        else:
                candidateballots[candidate] += 1
#calculate ballot percentages
percentage = (candidate (ballots/ totalballots)* 100 for candidate, ballots in candidateballots.item)
#Calculate winner
winner = max(candidateballots, key =candidateballots.get)
#Print results
print('Election Results')
print('-------------------')
print(f'Total Votes: {totalballots}')
print('-------------------')

