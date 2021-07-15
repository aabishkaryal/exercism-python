from datetime import *
from calendar import *

MeetupDayException = Exception

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

position = ["1st", "2nd", "3rd", "4th", "5th"]


def meetup(year, month, week, day_of_week):
    if (week in position):
        d = date(year, month, 1)
        while(d.strftime("%A") != day_of_week):
            d += timedelta(days=1)
        resultDate = d + timedelta(days=7*(position.index(week)))
        if resultDate.month != month:
            raise MeetupDayException("Non Existent")
        return resultDate
    elif (week == "last"):
        last_day = date(year, month, monthrange(year, month)[1])
        while(last_day.strftime("%A") != day_of_week):
            last_day -= timedelta(days=1)
        return last_day
    elif (week == "teenth"):
        d = date(year, month, 13)
        while(d.strftime("%A") != day_of_week):
            d += timedelta(days=1)
        return d
