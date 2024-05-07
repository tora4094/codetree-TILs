n = int(input())
dx = [1,-1, 0, 0]
dy = [0, 0, -1, 1]
x, y = 0, 0

for _ in range(n):
    p, d = tuple(input().split())        
    if p == 'E':
        dir_num = 0
    elif p == 'W':
        dir_num = 1
    elif p == "S":
        dir_num = 2
    else: # p == "N":
        dir_num = 3

    x += (dx[dir_num] * int(d))
    y += (dy[dir_num] * int(d))


print(x, y)


# x,y = 1,5 
# dir_num = 2
# dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# # if dir_num == 0:
# #     nx, ny = x + dx[0], y + dy[0]
# # elif dir_num == 1:
# #     nx, ny = x + dx[1], y + dy[1]
# # elif dir_num == 2:
# #     nx, ny = x-1, y
# # elif dir_num == 2:
# #     nx, ny = x, y+1


# nx = x + dx[dir_num]
# ny = y + dy[dir_num]