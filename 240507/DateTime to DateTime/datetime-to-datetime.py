def calculate_minutes(a, b, c):
    day = a
    hour = b
    minute = c
    result = day * 1440 + hour * 60 + minute
    return result


a,b,c = tuple(map(int,input().split()))

START_DAY = 11
START_HOUR = 11
START_MINUTE = 11

start_datetime = calculate_minutes(START_DAY,START_HOUR,START_MINUTE)
end_datetime = calculate_minutes(a,b,c)

if start_datetime > end_datetime:
    print(-1)

else:
    datetime_diff = end_datetime - start_datetime
    print(datetime_diff)