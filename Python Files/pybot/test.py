import datetime

date1 = '2016-10-26 11:53:08'

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

date2 = '2016-10-27 10:23:08'

date11 = datetime.datetime.strptime(date1, datetimeFormat)

date12 = datetime.datetime.strptime(date2,datetimeFormat)

timedelta = date11 - date12
hour1 = timedelta.days * 24

hours = (timedelta.seconds) / 3600

overall_hour = hour1 + hours
print(overall_hour , ' Hours')
print(datetime.datetime.now())