import csv
f = open('201704-citibike-tripdata.csv','r')
g = open('201705-citibike-tripdata.csv','r')
h = open('201706-citibike-tripdata.csv','r')

i = open('stationList.csv','w')

next(csv.reader(f))
next(csv.reader(g))
next(csv.reader(h))

stationList = []

for row in csv.reader(f):
	station = [int(row[3]),row[4],row[5],row[6]]
	if station not in stationList:
		stationList.append(station)
		print 'station id = ' + str(station[0])
	station = [int(row[7]),row[8],row[9],row[10]]
	if station not in stationList:
		stationList.append(station)
		print 'station id = ' + str(station[0])


for row in csv.reader(g):
	station = [int(row[3]),row[4],row[5],row[6]]
	if station not in stationList:
		stationList.append(station)
		print 'station id = ' + str(station[0])
	station = [int(row[7]),row[8],row[9],row[10]]
	if station not in stationList:
		stationList.append(station)
		print 'station id = ' + str(station[0])

for row in csv.reader(h):
	station = [int(row[3]),row[4],row[5],row[6]]
	if station not in stationList:
		stationList.append(station)
		print 'station id = ' + str(station[0])
	station = [int(row[7]),row[8],row[9],row[10]]
	if station not in stationList:
		stationList.append(station)
		print 'station id = ' + str(station[0])

print 'The number of station is ' + str(len(stationList))

temp = sorted(stationList, key=lambda x: x[0])
stationList = temp

for element in stationList:
	csv.writer(i).writerow(element)



