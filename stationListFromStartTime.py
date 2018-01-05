import csv
f = open('sortByStartTimeData.csv','r')

i = open('stationListFromStartTime.csv','w')

stationList = []
station = ['','','','']
for row in csv.reader(f):
	if len(row) >= 4:
		if row[3] != station[0]:
			station = [row[3],row[4],row[5],row[6]]
			stationList.append(station)
			print 'station id = ' + str(station[0]) + ' len = ' + str(len(stationList))
print 'The number of station is ' + str(len(stationList))

#stationList = sorted(stationList, key=lambda x: int(x[0]))

for element in stationList:
	csv.writer(i).writerow(element)