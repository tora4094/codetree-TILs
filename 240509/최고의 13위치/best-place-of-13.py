n = int(input())
a = [
    [0] * n
    for _ in range(n)
]

for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        a[i][j] = arr[j]

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        max_cnt = max(max_cnt, a[i][j] + a[i][j+1] + a[i][j+2])
print(max_cnt)
# n = 5
# arr = [[1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0],
#        [0, 1, 1, 0, 1],
#        [0, 0, 0, 1, 0],
#        [0, 0, 0, 0, 0]]

# max_cnt = 0
# for i in range(n): #행 
#     for j in range(n - 1): #열
#         max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1])

# print(max_cnt)

# >> 2