OFFSET = 100 
size = 201

n = int(input())
A = [[0 for _ in range(size)] for _ in range(size)]

for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            A[i][j] = 1

result = 0
for row in A:
    result += sum(row)    

print(result)


# OFFSET = 100

# n = int(input())
# A = [0] * 205

# for _ in range(n):
#     s, e = map(int,input().split())
#     s += OFFSET
#     e += OFFSET

#     # s ~ e-1
#     for i in range(s, e):
#         A[i] += 1
# print(max(A))