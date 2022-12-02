import time
import winsound

myTime = int(input("enter the time in seconds: "))

# reversed countdown
for x in range(myTime,0,-1):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Time IS UP!")
frequency = 2000
duration = 1000 #mseconds
winsound.Beep(frequency,duration)