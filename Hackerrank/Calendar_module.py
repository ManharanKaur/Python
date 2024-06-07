# Calendar Module
import calendar
date = list(map(int,input().split()))#MM DD YYYY
day = calendar.weekday(date[2],date[0],date[1])#YYYY,MM,DD
match day:
    case 0:
        print("MONDAY")
    case 1:
        print("TUESDAY")
    case 2:
        print("WEDNESDAY")
    case 3:
        print("THURSDAY")
    case 4:
        print("FRIDAY")
    case 5:
        print("SATURDAY")
    case 6:
        print("SUNDAY")
    case default:
        print(-1)
