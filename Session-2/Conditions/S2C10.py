def LeapYear(yr):
    if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
        return True
    else:
        return False


print(LeapYear(1910))
print(LeapYear(2012))
