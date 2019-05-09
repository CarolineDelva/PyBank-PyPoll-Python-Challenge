import os 
import csv

csvpath = os.path.join(".", "Python_challenge", "budget_data")

with open (csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    for row in csvreader:
        for (i,v) in enumerate (row):
            column[i].append(v)
            print(column[1])

