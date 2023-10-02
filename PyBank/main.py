#Import the data
import csv

#Read the csv file
with open('./Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)

    #create a list to manipulate the data
    csv_header = next(csvreader)
    list = []
    change = []
    
    #attach the second row to the list and remove the headers using pop
    for row in csvreader:
            #print(row[0], row[1]) #used only to verify the data was correctly impoted
            list.append(int(row[1]))
    
#print(list) #used only to verify the data in the list

#Ser the variable "profit"
    profit = 0

#Count and prin the total number of months
    for row in list:
        months = sum(1 for row in list)
    print("Total Months: ", months)

    #Sum and print the total profit in the changes
    for row in list:
        profit = profit + int(row)
    print("Total: $", profit)

    #Calculate the average change
    for x in range(1, len(list)):
         change.append((int(list[x]) - int(list[x-1])))
         
    average_change = sum(change) / len(change)
    print(average_change)

    #find the greates increase and decrease
    great_increase = max(change)
    great_decrease = min(change)
    print("Greatest Increase in Profits: ", great_increase)
    print("Greatest Decrease in Profits: ", great_decrease)