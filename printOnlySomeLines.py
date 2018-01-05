import csv
f = open('sortByStartTimeData.csv','r')
count = 0
for row in csv.reader(f):
	if int(row[3]) >=3633:
		print row[0:7]
		count = count + 1
	
	
