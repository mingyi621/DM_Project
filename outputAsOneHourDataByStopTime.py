import csv
f = open('sortByStopTimeData.csv','r')
w = open('outputAsOneHourDataByStopTime.csv','w')

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


'''
timeline = []
time = '2016-10-01 00:00:00'
timeline.append(time)
while stringToTimeStamp(time) < stringToTimeStamp('2017-10-31 23:59:59')
	time = timeStampToString(stringToTimeStamp(time) + 3600)
	timeline.append(time)
'''
# 328,2016-10-01 00:00:07,2016-10-01 00:05:35,471,Grand St & Havemeyer St,40.71286844,-73.95698119,3077,Stagg St & Union Ave,40.70877084,-73.95095259,25254,Subscriber,1992,1
# station = row[3]
# time = row[1]
# station, time, count

count = 0
time = '2016-10-01 00:00:00'
sta = ''
for row in csv.reader(f):
	if len(row) >= 7:
		if sta != row[7] and sta != '':
			print sta
			line = [sta, time, str(count)]
			csv.writer(w).writerow(line)
			time = timeStampToString(int(stringToTimeStamp(row[2])/3600)*3600)
			count = 0
		if stringToTimeStamp(row[2]) >= stringToTimeStamp(time)+3600:
			line = [row[7], time, str(count)]
			csv.writer(w).writerow(line)
			time = timeStampToString(int(stringToTimeStamp(row[2])/3600)*3600)
			count = 0
		sta = row[7]
		count = count + 1
		


