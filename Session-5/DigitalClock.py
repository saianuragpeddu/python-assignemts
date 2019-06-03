import time
seconds = 56
minutes = 59
hours = 3

while True:
    print('Tick', str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        print('Tock', str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
        minutes = minutes + 1
    if minutes == 60:
        minutes = 00
        hours = hours + 1
        print('Bong', str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
    if hours == 6:
        break
print('Three Hours Done')
