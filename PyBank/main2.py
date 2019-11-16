#Formating how the code will print
print("Financial Analysis")
print("-------------------------------------------")

#Importing dependencies
import os 
import csv


# Set path for files
csvpath = os.path.join('..', 'Resources', "budget_data.csv")


#Setting Total_months, first_number, last_number, and diff to 0 and creating an empty list
Total_months = 0 
Net_Profit_loss = []
first_number = 0 
last_number = 0 
diff = 0 
#1
#Reading csv
with open (csvpath, newline = "") as csvfile:
    budget_dataCsv = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    budgetDatalist = [row for row in budget_dataCsv]          
    
print("Total months :" + str(len(budgetDatalist)))







#2
#Reading csv
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    
    #Iterating over each line, and adding 1 when the Total_months is 0, and appending to the empty list    
    for line in reader:
        if Total_months==0:
            Total_months+= 1
        Net_Profit_loss.append(int (line[1]))

print("Net profit and loss: " + str(sum(Net_Profit_loss))+ " $")

#3
#Reading csv and creating empty lists
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    diffs = []
    #Iterating every line and append to the prof_los empty list
    for line in reader:
      prof_los.append(int(line[1]))
    #Creating try catch statements 
    for index, num in enumerate(prof_los):
      try:
       if index != 0:
        diff = abs(prof_los[index]) - abs(prof_los[index-1])
        diffs.append(diff)
      except Exception:
        continue
        #Assigning the average of differences to a variable and printing 
    average = sum(diffs)/len(diffs)
    print("Average change:" + str(average))


#3
#Reading csv and creating empty lists
with open (csvpath) as csvfile: 
    reader = csv.reader(csvfile)
    header = next(reader)
    prof_los = []
    months = []
    diffs = []
    #Iterating over every line
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



