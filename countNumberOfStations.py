import csv
f = open('outputAsOneHourDataByStartTimeWithZeros.csv','r')

station = ''
count = 0
#next(csv.reader(f))
for row in csv.reader(f):
	if station != row[0]:
		count = count + 1
		station = row[0]

print 'The number of stations is ' + str(count) 
x = 731* 24*(365)
print x
