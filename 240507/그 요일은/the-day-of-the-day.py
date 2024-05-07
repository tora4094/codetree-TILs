m1, d1, m2, d2 = tuple(map(int,input().split()))

def num_of_days(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    for i in range(1, m):
        total_days += days[i]

    total_days += d
    return total_days

diff = num_of_days(m2,d2) - num_of_days(m1,d1)

print(diff % 7)