import time
import datetime as dt
import os
def beep():
    if os.name=='nt': #windows
        import winsound
        winsound.Beep(600,2000) #2000milisec=1sec and 1000freq
    else:
        print('\a') #bell character

def timer(hours, minutes, seconds):
    print(f"Current Time: {dt.datetime.now().time().strftime('%Hh:%Mm:%Ss')}")
    time_in_seconds=hours*3600 + minutes*60 + seconds
    print(f"Timer set for : {hours}h {minutes}m {seconds}s")
    print(f"------STARTING------")
    while time_in_seconds>0:
        # print(f"{time_in_seconds} left")
        #converting left time to hr, min, secs
        hr, rem= divmod(time_in_seconds, 3600)
        min, secs=divmod(rem, 60)
        print(f"Time Remaining: {hr}h:{min}m:{secs}s")
        time.sleep(1)
        time_in_seconds-=1

    print("TIME'S UP!!!!")
    print(f"Current time: {dt.datetime.now().strftime('%Hh:%Mm:%Ss')}")
    beep()

hours=int(input("Enter time in hours:"))
minutes=int(input("Enter time in minutes:"))
seconds=int(input("Enter time in seconds:"))
timer(hours,minutes,seconds)