import csv
f = open('outputAsOneHourDataByStopTime.csv')
w = open('outputAsOneHourDataByStopTimeWithZeros.csv','w')

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
#		print t
	else:
		print 'nothing'

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


# 72, 2016-10-01 00:00:00, number

allData = []
time = '2016-10-01 00:00:00'
station = '72'
for row in csv.reader(f):
	if station != row[0]:
		while stringToTimeStamp(time) < stringToTimeStamp('2017-10-01 00:00:00'):
			allData.append([station, time, '0'])
			time = timeStampToString(stringToTimeStamp(time) + 3600)
		station = row[0]
		time = '2016-10-01 00:00:00'
		print station
	while row[1] != time and stringToTimeStamp(time) < stringToTimeStamp('2017-10-01 00:00:00'):
		allData.append([station, time, '0'])
		time = timeStampToString(stringToTimeStamp(time) + 3600)
	if stringToTimeStamp(time) >= stringToTimeStamp('2017-10-01 00:00:00'):
		continue
	allData.append(row)
	time = timeStampToString(stringToTimeStamp(time) + 3600)

for element in allData:
	csv.writer(w).writerow(element)









