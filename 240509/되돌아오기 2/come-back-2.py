x,y = 0,0
dxs, dys = [1,0,-1,0],[0,-1,0,1]

A = list(input())

cnt = 0
result = -1 

dir_num = 3 

for d in A:
    if cnt != 0 and x == 0 and y == 0:
        result = cnt
        break
    if d == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]        
    elif d == 'L':
        dir_num = (dir_num - 1) % 4
    elif d == 'R':
        dir_num = (dir_num + 1) % 4
    cnt += 1

print(result)