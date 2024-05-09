r, c = tuple(map(int,input().split()))

a = [
    input().split()
    for _ in range(r)
]

result = 0
for i in range(1, r-1):
    for j in range(1,c-1):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if a[0][0] != a[i][j] and a[i][j] != a[k][l] and a[k][l] != a[-1][-1]:
                    result += 1
print(result)

# n = 5
# arr = [[1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0],
#        [0, 1, 1, 0, 1],
#        [0, 0, 0, 1, 0],
#        [0, 0, 0, 0, 0]]

# max_cnt = 0
# for i in range(n):
#     for j in range(n - 1):
#         for k in range(i + 1, n):
#             for l in range(n - 1):
#                 max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1]
#                                      + arr[k][l] + arr[k][l + 1])

# print(max_cnt)