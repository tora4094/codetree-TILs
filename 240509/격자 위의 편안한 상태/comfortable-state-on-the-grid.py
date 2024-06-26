N, M = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt

for _ in range(M):
    r, c = map(int, input().split())
    arr[r][c] = 1
    if adjacent_cnt(r, c) == 3:
        print(1)
    else:
        print(0)