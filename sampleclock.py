import time
seconds = 56
minutes = 59
hours = 3

while True:
    print('Tick')
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        print('Tock', )
        minutes = minutes + 1
    if minutes == 60:
        minutes = 00
        hours = hours + 1
        print('Bong')
    if hours == 6:
        break
print('Three Hours Done')
