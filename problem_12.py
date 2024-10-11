


def timeConversion(s):
    if s[-2:] == "PM" and int(s[:2]) < 12:
        return str(int(s[:2]) + 12) + s[2:-2]
    else:
        if s[-2:] == "AM" and int(s[:2]) == 12:
            return "00" + s[2:-2]
        else:
            return s[:-2]
    
print(timeConversion("07:05:45PM"))
    