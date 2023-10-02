import csv

with open('./Resources/budget_data.csv') as data_file:
    csvreader = csv.reader(data_file)

    list = []
    flag = True
    profit = 0

    for row in csvreader:
            #print(row[0], row[1])
            if flag == True:
                  flag = False
                  pass
            else:
                 profit = profit + float(row[1]) 
            
            #list.append(row[1])
#list.pop(0)

#profit = 0
#for row in list:
 #     profit = profit + float(row)
print(profit)

#print(list)