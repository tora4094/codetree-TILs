n,k = map(int,input().split())

blocks = [0] * n

for _ in range(k):
    a, b = map(int,input().split())
    for i in range(a-1, b):
        blocks[i] += 1
print(max(blocks))