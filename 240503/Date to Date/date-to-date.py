m1, d1, m2, d2 = map(int,input().split())

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if m1 == m2:
    print(d2 - d1 + 1)

else:
    total_days = 0
    total_days += (month_days[m1] - d1 + 1)
    total_days += d2
    for month in range(m1 + 1, m2):
        total_days += month_days[month]

    print(total_days)