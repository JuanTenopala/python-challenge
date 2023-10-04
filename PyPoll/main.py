import csv

with open('./Resources/election_data.csv') as data_file:
    csvreader = csv.reader(data_file)
    
    csv_header = next(csvreader)
    id = []
    candidate = []

    for row in csvreader:
        id.append(row[0])
        candidate.append(row[2])

    votes = len(id)
    print(votes)

    #set = set(candidate)
    #print(set)
    '''
    {'Raymon Anthony Doane', 'Diana DeGette', 'Charles Casper Stockham'}
    '''
    
    votes_count = {}
    for item in candidate:
        votes_count[item] = votes_count.get(item, 0) + 1  

    winner_name = []
    winner_percentage = []
    for item, count in votes_count.items():
        percent = item, (count / votes)*100, count
        print(percent)


        winner_name.append(item)
        winner_percentage.append(count)

    print(winner_name[winner_percentage.index(max(winner_percentage))])

