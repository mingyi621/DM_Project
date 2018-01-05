import csv
f = open('outputAsOneHourData.csv','r')
stationList = []
for row in csv.reader(f):
	if row[0] not in stationList:
		stationList.append(row[0])
print len(stationList)
