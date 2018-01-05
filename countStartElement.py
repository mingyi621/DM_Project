import csv
f = open('outputAsOneHourDataByStopTime.csv','r')

count = 0
for row in csv.reader(f):
	if len(row) <= 2:
		continue
	count = count + int(row[2])
print count