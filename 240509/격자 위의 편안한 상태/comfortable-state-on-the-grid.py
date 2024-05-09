N, M = tuple(map(int,input().split()))

arr = [
    [0] * (N + 1)
    for _ in range(N+1)
]

dxs, dys = [0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 1 <= x <= N and 1 <= y <= N

def adjacent_cnt(x,y):
    cnt = 0
    result = 0
    for dx, dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy        
        if in_range(nx,ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt >= 3:
        result = 1
    return result

for _ in range(M):
    r, c = tuple(map(int,input().split()))    
    if in_range(r,c):
        arr[r][c] = 1    
        print(adjacent_cnt(r,c))