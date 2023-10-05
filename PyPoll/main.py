# Import the data
import csv

#Read the CSV file
with open('./Resources/election_data.csv') as data_file:
    csvreader = csv.reader(data_file)
    csv_header = next(csvreader)
    
    # Create the lists to manipulate the data
    id = []
    candidate = []

    #attach the rows to it's respective lists
    for row in csvreader:
        id.append(row[0])
        candidate.append(row[2])

    # Count the number of registered votes
    votes = len(id)
    #print(votes)
    
    # Count the votes per candidate
    votes_count = {}
    for item in candidate:
        votes_count[item] = votes_count.get(item, 0) + 1  

    # Concatenate the candidate, the percentage of votes and the total number of votes
    results = []
    winner_name = []
    winner_percentage = []
    for item, count in votes_count.items():
        percent = round((count / votes)*100, 3)
        result = f"{item}, {percent}%, ({count})"
        results.append(result)

    # Determine the winer candidate
        winner_name.append(item)
        winner_percentage.append(percent)



# Save the results into variables to print
total_votes = f"Total votes: ", votes
result = "\n".join(results)
winner = winner_name[winner_percentage.index(max(winner_percentage))]

# Print results
print("Election Results")
print("-------------------------")
print("total votes: ", total_votes)
print("-------------------------")
print(result)
print("-------------------------")
print("Winner: ", winner)

# Export the results to a text file
with open ("PyPoll.txt", "w") as f:
    f.write("Election Results" + "\n")
    f.write("-------------------------" + "\n")
    f.write("total votes: " + str(total_votes) + "\n")
    f.write("-------------------------" + "\n")
    f.write(str(result) + "\n")
    f.write("-------------------------" + "\n")
    f.write("Winner: " + str(winner) + "\n")