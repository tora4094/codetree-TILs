# 4 * 4

arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))

sum_val1 = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr[i])):
        sum_val1 += arr[i][j]

sum_val2 = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        sum_val2 += arr[i][j]

result = sum_val2 - sum_val1
print(result)