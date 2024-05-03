OFFSET = 100

n = int(input())
A = [0] * 205

for _ in range(n):
    s, e = map(int,input().split())
    s += OFFSET
    e += OFFSET

    # s ~ e-1
    for i in range(s, e):
        A[i] += 1
print(max(A))