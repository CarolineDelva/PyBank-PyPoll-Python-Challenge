#modules
print("Financial Analysis")
print("-------------------------------------------")

import os 
import csv


# Set path for files
csvpath = os.path.join('..', 'Resources', "budget_data.csv")

Total_months = 0 
Net_Profit_loss = []
first_number = 0 
last_number = 0 
diff = 0 
#1
with open (csvpath, newline = "") as csvfile:
    budget_dataCsv = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    budgetDatalist = [row for row in budget_dataCsv]          
    
print("Total months :" + str(len(budgetDatalist)))







#2
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
        
    for line in reader:
        if Total_months==0:
            Total_months+= 1
        Net_Profit_loss.append(int (line[1]))

print("Net profit and loss: " + str(sum(Net_Profit_loss))+ " $")

#3
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    diffs = []
    for line in reader:
      prof_los.append(int(line[1]))
    
    for index, num in enumerate(prof_los):
      try:
       if index != 0:
        diff = abs(prof_los[index]) - abs(prof_los[index-1])
        diffs.append(diff)
      except Exception:
        continue
    average = sum(diffs)/len(diffs)
    print("Average change:" + str(average))


#3
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    months = []
    diffs = []
    for line in reader:
      prof_los.append(int(line[1]))
      months.append(line[0])
    
    for index, num in enumerate(prof_los):
      try:
       if index != 0:
        diff = prof_los[index] - prof_los[index-1]
        diffs.append(diff)
      except Exception:
        continue
    max = max(diffs)
    min = min(diffs)

    max_index = diffs.index(max) + 1
    min_index = diffs.index(min) + 1

    print("Greatest Increase in Profits: " + months[max_index],max)
    print("Greatest Decrease in Profits: " + months[min_index], min)



