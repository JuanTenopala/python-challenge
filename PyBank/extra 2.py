import csv

with open('./Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)
    
    row_count = sum(1 for row in csvreader)
    profit = 0
    next(csvreader,None)
    for row in csvreader:
        
        #print(row[0], row[1])
            
        profit = profit + float(row[1]) 
            
            #list.append(row[1])
#list.pop(0)

#profit = 0
#for row in list:
 #     profit = profit + float(row)
    print(row_count)
print(profit)