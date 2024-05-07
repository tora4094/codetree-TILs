mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
n, t = tuple(map(int,input().split()))
r,c,d = tuple(input().split())
r, c = int(r), int(c)
d = mapper[d]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def in_range(x,y):
    return 1 <= x <= n and 1 <= y <= n

for _ in range(t):
    nr = r + dx[d]
    nc = c + dy[d]

    if in_range(nr, nc):
        r, c = nr, nc
    else:
        d = 3 - d

print(r, c)






# n = 5
# x, y = 1, 2
# dir_num = 2

# dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]


# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n


# while keep_moving():
#     nx, ny = x + dxs[dir_num], y + dys[dir_num]
#     if not in_range(nx, ny):  # check whether position is out of grid
#         dir_num = 3 - dir_num # change direction
    
#     # move
#     x, y = x + dxs[dir_num], y + dys[dir_num]