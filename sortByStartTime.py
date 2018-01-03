import csv
s = open('stationList.csv','r')
f = open('201704-citibike-tripdata.csv','r')
g = open('201705-citibike-tripdata.csv','r')
h = open('201706-citibike-tripdata.csv','r')

w = open('sortByStartTimeData.csv','w')

next(csv.reader(f))
next(csv.reader(g))
next(csv.reader(h))

def stringToTimeStamp(t): # time = '2017-04-01 00:01:54'
	t = t.split(' ')
	date = t[0].split('-')
	time = t[1].split(':')
	year = int(date[0])
	month = int(date[1])
	day = int(date[2])
	hour = int(time[0])
	minute = int(time[1])
	second = int(time[2])

	if month == 4:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400
	elif month == 5:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + 30 * 86400
	elif month == 6:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (30 + 31) * 86400
	else:
		print 'nothing'

	return timeStamp

stationList = []

for row in csv.reader(s):
	stationList.append(row)

allData = []
for row in csv.reader(f):
	allData.append(row)
for row in csv.reader(g):
	allData.append(row)
for row in csv.reader(h):
	allData.append(row)

for station in stationList:
	print 'station id = ' + station[0]
	oneStationData = []
	for element in allData:
		if station[0] == element[3]:
			oneStationData.append(element)
	temp = sorted(oneStationData, key=lambda x: stringToTimeStamp(x[1]))
	oneStationData = temp
	for data in oneStationData:
		csv.writer(w).writerow(data)








