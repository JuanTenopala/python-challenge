#Import the data
import csv

#Read the csv file
with open('./Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)

    #create a list to manipulate the data
    csv_header = next(csvreader)
    change = []
    date = []
    

    for row in csvreader:
         change.append(int(row[1]))
         date.append(row[0])

    months = len(date)
    print("Total Months:",months)

    total = sum(change)   #print(str(sum(change)))
    print("Total: $",total)
         
         
    revenue_change = []

    for x in range(1, len(change)):
         revenue_change.append((int(change[x]) - int(change[x-1])))

    #Calculate the average change
    average_change = sum(revenue_change) / (len(change)-1)
    print("Average Change: $",average_change)

    #find the greates increase and decrease
    great_increase = max(revenue_change)
    great_decrease = min(revenue_change)
    great_increase_index = revenue_change.index(great_increase)
    great_decrease_index = revenue_change.index(great_decrease)
    month_great_increase = date[great_increase_index + 1]
    month_great_decrease = date[great_decrease_index + 1]
    print("Greatest Increase in Profits:", month_great_increase, "($", great_increase, ")")
    print("Greatest Decrease in Profits:", month_great_decrease, "($", great_decrease, ")")