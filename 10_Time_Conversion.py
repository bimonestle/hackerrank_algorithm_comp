# Given a time in 12-hour AM/PM format,
# convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example:
# s = '12:01:00PM'
# return '12:01:00'
# s = '12:01:00AM'
# return '00:01:00'

def timeConversion(s):
    formatPos = len(s)-2
    
    time = s[:formatPos]
    timeFormat = s[-2:]
    
    timeSplit = time.split(":")
    hour = int(timeSplit[0])
    
    if timeFormat == 'AM' and hour >= 12:
        hour -= 12
        if hour < 10:
            timeSplit[0] = '0' + str(hour)
    elif timeFormat == 'PM' and hour < 12:
        hour += 12
        timeSplit[0] = str(hour)
        
    return ":".join(timeSplit)