n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(n, x, y):
    return 0 <= x <= n and 0 <= y <= n

x, y = 0, 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

cnt = 0
result = 0
for i in range(n-1):
    for j in range(n-1):
        x, y = i, j
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(n, nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            #print(f"{x+1}행{y+1}열에 인접한 칸 중 숫자 1의 개수는 {cnt}개 입니다.")
            result += 1
    cnt = 0

print(result)
# x, y = 2, 1
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# cnt = 0

# for dir_num in range(4):
#     nx = x + dx[dir_num]
#     ny = y + dy[dir_num]
#     if A[nx][ny] == 1:
#         cnt += 1

# a = [[0, 0, 0, 1, 0],
#      [0, 1, 1, 1, 0],
#      [0, 0, 0, 0, 1],
#      [1, 0, 1, 1, 1],
#      [1, 0, 1, 1, 0]]

# x, y = 2, 1
# dxs = [0, 1, 0, -1]
# dys = [1, 0, -1, 0]

# def in_range(x, y):
#     return 0 <= x < 5 and 0 <= y < 5

# cnt = 0
# for dx,dy in zip(dxs, dys):
#     nx, ny = x + dx, y + dy
#     if in_range(nx,ny) and a[nx][ny] == 1:
#         cnt += 1