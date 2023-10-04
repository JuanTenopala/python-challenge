#Import the data
import csv

#Read the csv file
with open('./Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)

    #create a list to manipulate the data
    csv_header = next(csvreader)
    change = []
    date = []
    
     # Attatch the rows to its respective list adding the data type integer to row 1
    for row in csvreader:
         change.append(int(row[1]))
         date.append(row[0])

     # Calculate the total number of months
    months = len(date)
    
     # Calculate the total revenue
    total = sum(change)   #print(str(sum(change)))
    
    # Create a list for the changes in the revenue              
    revenue_change = []

     # Attach the changes in revenue to the list
    for x in range(1, len(change)):
         revenue_change.append((int(change[x]) - int(change[x-1])))

    # Calculate the average change
    average_change = sum(revenue_change) / (len(change)-1)
    

    #find the greates increase and decrease
    great_increase = max(revenue_change)
    great_decrease = min(revenue_change)
    great_increase_index = revenue_change.index(great_increase)
    great_decrease_index = revenue_change.index(great_decrease)
    month_great_increase = date[great_increase_index + 1]
    month_great_decrease = date[great_decrease_index + 1]


     # Print the results
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:",months)
    print("Total: $",total)
    print("Average Change: $",average_change)
    print("Greatest Increase in Profits:", month_great_increase, "($", great_increase, ")")
    print("Greatest Decrease in Profits:", month_great_decrease, "($", great_decrease, ")")

     # Export the results to a text file
    with open("PyBank.txt", "w") as f:
              f.write("Financial Analysis" + "\n")
              f.write("----------------------------" + "\n")
              f.write("Total Months: " + str(months) + "\n")
              f.write("Total: $" + str(total) + "\n")
              f.write("Average Change: $" + str(average_change) + "\n")
              f.write("Greatest Increase in Profits: " + str(month_great_increase) + " " + "$" + str(great_increase) + "\n")
              f.write("Greatest Decrease in Profits: " + str(month_great_decrease) + " " + "$" + str(great_decrease) + "\n")