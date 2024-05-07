m1, d1, m2, d2 = tuple(map(int,input().split()))

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

weekdays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# 1월 1일 월요일
start_weekday = 1

def count_days(m1, d1, m2, d2):
    days = 0
    if m1 == m2:
        days = d2 - d1
    else:
        days += (month_days[m1] - d1)
        for m in range(m1 + 1, m2):
            days += month_days[m]

        days += d2 - 1
    return days

days = count_days(m1, d1, m2, d2)

weekday_index = (start_weekday + days) % 7
weekday = weekdays[weekday_index]
print(weekday)