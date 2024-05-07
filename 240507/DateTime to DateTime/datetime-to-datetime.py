a,b,c = tuple(map(int,input().split()))

START_DAY = 11
START_HOUR = 11
START_MINUTE = 11

if a < START_DAY or b < START_HOUR or c < START_MINUTE:
    print(-1)
else:
    day_diff = a - START_DAY
    hour_diff = b - START_HOUR
    minute_diff = c - START_MINUTE
    total_minutes = day_diff * 1440 + hour_diff * 60 + minute_diff
    print(total_minutes)