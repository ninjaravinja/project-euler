import datetime

start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)

current = start
sunday_count = 0

while current <= end:
    if current.weekday() == 6 and current.day == 1:
        sunday_count += 1
    current += datetime.timedelta(days=1)

print(sunday_count)