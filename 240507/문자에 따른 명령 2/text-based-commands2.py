x, y = (0, 0)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = 3

arr = list(input())
for elem in arr:
    if elem == 'L':
        dir_num = (dir_num - 1 + 4) % 4      
    elif elem == 'R':
        dir_num = (dir_num + 1) % 4      
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x,y)

# x, y = (1,5)
# dir_num = ??

# # 시계방향으로 90도 회전
# dx = [1, 0, -1, 0]
# dy = [0, -1 ,0, 1]

# # 다음방향 
# dir_num = (dir_num + 1) % 4

# x += dx[dir_num]
# y += dy[dir_num]

# #python
# dir_num = (dir_num - 1) % 4

# #java, c++ 
# dir_num = (dir_num - 1 + 4) % 4