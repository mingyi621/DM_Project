import csv
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

f = open('sortByStartTimeData.csv','r')

count = 0
for row in csv.reader(f):
	count = count + 1
print count

count_origin = 0
for row in csv.reader(f_1610):
	count_origin = count_origin + 1
for row in csv.reader(f_1611):
	count_origin = count_origin + 1
for row in csv.reader(f_1612):
	count_origin = count_origin + 1
for row in csv.reader(f_1701):
	count_origin = count_origin + 1
for row in csv.reader(f_1702):
	count_origin = count_origin + 1
for row in csv.reader(f_1703):
	count_origin = count_origin + 1
for row in csv.reader(f_1704):
	count_origin = count_origin + 1
for row in csv.reader(f_1705):
	count_origin = count_origin + 1
for row in csv.reader(f_1706):
	count_origin = count_origin + 1
for row in csv.reader(f_1707):
	count_origin = count_origin + 1
for row in csv.reader(f_1708):
	count_origin = count_origin + 1
for row in csv.reader(f_1709):
	count_origin = count_origin + 1

print count_origin