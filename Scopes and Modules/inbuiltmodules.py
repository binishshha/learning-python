# python has a lot of inbuilt module that makes our experience easier and flexible

#-------------datetime module-------------
import datetime as dt

#---date using datetime module------
date=dt.date(2026,1,11)
#datetime module has a class date which takes year, month,day as parameters 
#so we create date object and pass it to a class 
print(f"the date i entered is : {date}")

# get today's date using today() method from date class
print(f"today's date is: {dt.date.today()}")

# access a specific part of today's date
print(f"current year:{dt.date.today().month}")

# OR store todays date in a variable and access it easily
today=dt.date.today()
print(f"today's day:{today.day}")

#------both date and time using datetime module-----
#datetime is a class and we created date as an object an pass all required parameters through a constructor
date=dt.datetime(2026,1,11,1,11,11)
print(date)
#displays full current date and time
current_datetime=dt.datetime.now()
print(current_datetime)
print(f"current date:{dt.datetime.now().date()}")
print(f"current time:{current_datetime.time()}")
print(f"current time in hours:{current_datetime.hour}")
print(f"current time in minutes:{current_datetime.minute}")
print(f"current time in seconds:{current_datetime.second}")

#------------time module---------
import time as t

time=t.time()
print(f"current time in seconds:{time}") #the second is being calculated since 1970,jan 1st

#-------formatting datetime objects, converting string ti date and time--------
# first of all import datetime module which is already done
#-----------converting  string to datetime ---------
#use strptime to parse a string value to datetime object in a way string value is
date1= "2026-1-11 1:11:11"
print(date)

print(F"type of date1 before formatting:{type(date1)}") #<class 'str'>
formatted1=dt.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
print(formatted1) #2026-01-11 01:11:11
print(F"type after formatting date1:{type(formatted1)}") #  <class 'datetime.datetime'>

#----------converting datetime to string-------
#use strftime to convert a datetime obj to a string value you want
date2=dt.datetime.now()
print(date2)
print(f"type of date2 before formatting: {type(date2)}") # <class 'datetime.datetime'>
formatted2=date2.strftime("%d day, %m month, %y year or %Y year, and %H hours, %M minutes, %S seconds")
print(f"after fromatting datetime object  to string :\n{formatted2}")
print(f"type after formatting date2: {type(formatted2)}")  #<class 'str'>

#-----------using arithmetic operations on datetime module-------
# we can use timedelta() to specify duration only

# datetime-timedelta -> datetime
# datetime+timedelta -> datetime
# datetime-datetime -> timedelta

datenow=dt.datetime.now()

dateafter=datenow+dt.timedelta(days=5, hours=2)
print(f"current datetime:{datenow}")
print(f"date after 5days and 2 hours:{dateafter}")

birthdate=dt.datetime(2006,9,11)

time_diff=datenow-birthdate
print(f"time difference between {datenow} and {birthdate} : {time_diff}")
# we can convert the time difference into years
age=time_diff.days/365
print(f"Current age: {age}")

#-----timezone-------
# represents how far is the time from utc

current_time=dt.datetime.now(dt.timezone.utc)
print(f"UTC time currently: {current_time}")

#time that is 5 hours ahead of utc
fiveutc=dt.timezone(dt.timedelta(hours=5))
# print(fiveutc) #just prints the difference in utc time
time=dt.datetime.now(fiveutc)
print(time)

#NEPAL TIME
nepaltime=dt.datetime.now(dt.timezone(dt.timedelta(hours=5 , minutes=45)))
print(f"Nepal time as per utc time: {nepaltime}")

