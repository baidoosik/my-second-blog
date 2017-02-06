import csv

with open('egg.csv',newline='') as csvfile:
    lylics = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for a in lylics:
        print(a)

