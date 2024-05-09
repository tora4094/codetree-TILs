N = int(input())
D = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}
dxs, dys = [1,0,-1,0],[0,-1,0,1]
x, y = 0, 0
cnt = 0
result = -1
for _ in range(N):    
    position,number = tuple(input().split())
    number = int(number)
    for _ in range(number):            
        dir_num = D[position]
        x += dxs[dir_num]
        y += dys[dir_num]
        cnt += 1
        if x == 0 and y == 0:
            result = cnt
            break
    if result != -1:
        break

print(result)