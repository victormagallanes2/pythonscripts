from datetime import datetime, timedelta


day = '17/Oct/2020'

dt = datetime.strptime(day, '%d/%b/%Y')

start = dt - timedelta(days=dt.weekday())

end = start + timedelta(days=6)

print(start)
print(end) 