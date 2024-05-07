n,m = tuple(map(int,input().split()))
answer = [
    [0] * m
    for _ in range(n)
]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

x, y = 0, 0
dir_num = 0

answer[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x, y = x + dx[dir_num], y + dy[dir_num]
    answer[x][y] = i

for i in range(n):
    print(*answer[i])
    # for j in range(m):
    #     print(answer[i][j], end = ' ')
    # print()