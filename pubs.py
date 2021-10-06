
import csv
import random

pubs_list = []

with open("open_pubs.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count=0

    for row in csv_reader:
        pubs_list.append(row[1])

x = len(pubs_list)
y=random.randint(0,x)
print (pubs_list[y])

    


