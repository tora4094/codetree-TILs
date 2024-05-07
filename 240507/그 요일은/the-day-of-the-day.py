m1, d1, m2, d2 = tuple(map(int,input().split()))
w = input()

def num_of_days(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    for i in range(1, m):
        total_days += days[i]

    total_days += d
    return total_days

diff = num_of_days(m2,d2) - num_of_days(m1,d1)
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
week_index = day_of_week.index(w)
a = diff % 7
if a < 0:
    a += 7

a_days = 0
if a <= diff:
    result = 1 + (diff - a) // 7

print(result)