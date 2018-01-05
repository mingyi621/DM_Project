import csv
import time
time_start = time.clock()
f_1610 = open('201610-citibike-tripdata.csv','r')
f_1611 = open('201611-citibike-tripdata.csv','r')
f_1612 = open('201612-citibike-tripdata.csv','r')
f_1701 = open('201701-citibike-tripdata.csv','r')
f_1702 = open('201702-citibike-tripdata.csv','r')
f_1703 = open('201703-citibike-tripdata.csv','r')
f_1704 = open('201704-citibike-tripdata.csv','r')
f_1705 = open('201705-citibike-tripdata.csv','r')
f_1706 = open('201706-citibike-tripdata.csv','r')
f_1707 = open('201707-citibike-tripdata.csv','r')
f_1708 = open('201708-citibike-tripdata.csv','r')
f_1709 = open('201709-citibike-tripdata.csv','r')

w_1 = open('sortByStartTimeData.csv','w')

next(csv.reader(f_1610))
next(csv.reader(f_1611))
next(csv.reader(f_1612))
next(csv.reader(f_1701))
next(csv.reader(f_1702))
next(csv.reader(f_1703))
next(csv.reader(f_1704))
next(csv.reader(f_1705))
next(csv.reader(f_1706))
next(csv.reader(f_1707))
next(csv.reader(f_1708))
next(csv.reader(f_1709))

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

	if year == 2016 and month == 10:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400
	elif year == 2016 and month == 11:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + 31 * 86400
	elif year == 2016 and month == 12:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30) * 86400
	elif year == 2017 and month == 1:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31) * 86400
	elif year == 2017 and month == 2:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31) * 86400
	elif year == 2017 and month == 3:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28) * 86400
	elif year == 2017 and month == 4:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28 + 31) * 86400
	elif year == 2017 and month == 5:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28 + 31 + 30) * 86400
	elif year == 2017 and month == 6:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28 + 31 + 30 + 31) * 86400
	elif year == 2017 and month == 7:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28 + 31 + 30 + 31 + 30) * 86400
	elif year == 2017 and month == 8:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28 + 31 + 30 + 31 + 30 + 31) * 86400
	elif year == 2017 and month == 9:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31) * 86400
	elif year == 2017 and month == 10:
		timeStamp = second + minute * 60 + hour * 3600 + day * 86400 + (31 + 30 + 31 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30) * 86400
		print t
	else:
		print t

	return timeStamp

def timeStampToString(timeStamp): # time = '2017-04-01 00:01:54'
	second = timeStamp % 60 # 1 min = 60 seconds
	timeStamp = timeStamp / 60
	minute = timeStamp % 60 # 1 hour = 60 mins
	timeStamp = timeStamp / 60
	hour = timeStamp % 24 # 1 day = 24 hours
	timeStamp = timeStamp / 24
	#(31 + 30 + 31 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30)
	if timeStamp <= 31:
		day = timeStamp
		month = 10
		year = 2016
	elif timeStamp <= 31+30:
		day = timeStamp % 31
		month = 11
		year = 2016
	elif timeStamp <= 31+30+31:
		day = timeStamp % (31+30)
		month = 12
		year = 2016
	elif timeStamp <= 31+30+31+31:
		day = timeStamp % (31+30+31)
		month = 1
		year = 2017
	elif timeStamp <= 31+30+31+31+28:
		day = timeStamp % (31+30+31+31)
		month = 2
		year = 2017
	elif timeStamp <= 31+30+31+31+28+31:
		day = timeStamp % (31+30+31+31+28)
		month = 3
		year = 2017
	elif timeStamp <= 31+30+31+31+28+31+30:
		day = timeStamp % (31+30+31+31+28+31)
		month = 4
		year = 2017
	elif timeStamp <= 31+30+31+31+28+31+30+31:
		day = timeStamp % (31+30+31+31+28+31+30)
		month = 5
		year = 2017
	elif timeStamp <= 31+30+31+31+28+31+30+31+30:
		day = timeStamp % (31+30+31+31+28+31+30+31)
		month = 6
		year = 2017
	elif timeStamp <= 31+30+31+31+28+31+30+31+30+31:
		day = timeStamp % (31+30+31+31+28+31+30+31+30)
		month = 7
		year = 2017
	elif timeStamp <= 31+30+31+31+28+31+30+31+30+31+31:
		day = timeStamp % (31+30+31+31+28+31+30+31+30+31)
		month = 8 
		year = 2017
	elif timeStamp <= 31+30+31+31+28+31+30+31+30+31+31+30:
		day = timeStamp % (31+30+31+31+28+31+30+31+30+31+31)
		month = 9
		year = 2017
	else:
		day = timeStamp % (31+30+31+31+28+31+30+31+30+31+31+30)
		month = 10
		year = 2017
	return str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2) + ' ' + str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)


#stationList = []

#for row in csv.reader(s):
#	stationList.append(row)

allData = []

print '1610'
for row in csv.reader(f_1610):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1611'
for row in csv.reader(f_1611):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1612'
for row in csv.reader(f_1612):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1701'
for row in csv.reader(f_1701):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1702'
for row in csv.reader(f_1702):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1703'
for row in csv.reader(f_1703):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1704'
for row in csv.reader(f_1704):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1705'
for row in csv.reader(f_1705):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1706'
for row in csv.reader(f_1706):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1707'
for row in csv.reader(f_1707):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1708'
for row in csv.reader(f_1708):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)
print '1709'
for row in csv.reader(f_1709):
	if len(row) > 3:
		allData.append(row)
	else:
		print len(row)

print 'Length of allData = ' + str(len(allData))
'''
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
'''
print 'Start sorting StartTime.'
allData = sorted(allData, key=lambda x: (int(x[3]), stringToTimeStamp(x[1])))
print 'Sorted.'

'''
t = ''
for element in allData:
	if t != element[3]:
		print element[3]
		t = element[3]
	csv.writer(w_1).writerow(element)
'''

w = open('outputAsOneHourDataByStartTime.csv','w')

count = 0
time = '2016-10-01 00:00:00'
sta = ''
for row in allData:
	if len(row) >= 4:
		if sta != row[3] and sta != '':
			print sta
			line = [sta, time, str(count)]
			csv.writer(w).writerow(line)
			time = timeStampToString(int(stringToTimeStamp(row[1])/3600)*3600)
			count = 0
		if stringToTimeStamp(row[1]) >= stringToTimeStamp(time)+3600:
			line = [row[3], time, str(count)]
			csv.writer(w).writerow(line)
			time = timeStampToString(int(stringToTimeStamp(row[1])/3600)*3600)
			count = 0
		sta = row[3]
		count = count + 1
line = [sta, time, str(count)]
csv.writer(w).writerow(line)


i = open('stationListFromStartTime.csv','w')

stationList = []
station = ['','','','']
for row in allData:
	if len(row) >= 4:
		if row[3] != station[0]:
			station = [row[3],row[4],row[5],row[6]]
			stationList.append(station)
			print 'station id = ' + str(station[0]) + ' len = ' + str(len(stationList))
print 'The number of station is ' + str(len(stationList))

#stationList = sorted(stationList, key=lambda x: int(x[0]))

for element in stationList:
	csv.writer(i).writerow(element)


print 'StartTime Done.'

print time.clock() - time_start


