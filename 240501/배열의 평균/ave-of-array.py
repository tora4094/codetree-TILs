n = 2 
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    sum_val = 0 
    for j in range(4):
        sum_val += arr[i][j]
    h_avg = sum_val / 4
    print(f"{h_avg:.1f}",end=" ")
print()

for i in range(4):
    sum_val = 0
    for j in range(n):
        sum_val += arr[j][i]
    v_avg = sum_val / 2
    print(f"{v_avg:.1f}",end=" ")
print()

sum_val = 0
for i in range(n):
    for j in range(4):
        sum_val += arr[i][j]
avg = sum_val / (n*4)
print(f"{avg:.1f}")