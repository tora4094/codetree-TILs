n,m = 3,3

arr1 = [list(map(int,input().split())) for _ in range(n)]
input()
arr2 = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        result = arr1[i][j] * arr2[i][j]
        print(result, end=" ")
    print()