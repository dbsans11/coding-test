import datetime
solution = lambda a,b: ['MON','TUE','WED','THU','FRI','SAT','SUN'][datetime.date(2016,a,b).weekday()]