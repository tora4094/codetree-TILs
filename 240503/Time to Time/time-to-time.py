hour1, min1, hour2, min2 = map(int,input().split())
start_min = hour1 * 60 + min1
end_min = hour2 * 60 + min2

min_diff = end_min - start_min
print(min_diff)