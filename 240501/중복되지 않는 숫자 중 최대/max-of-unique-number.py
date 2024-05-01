n = int(input())
arr = list(map(int,input().split()))
result = -1
arr.sort()
for elem in arr:
    if result == -1:
        result = elem
    elif result == elem:
        result = -1
    elif elem > result:
        result = elem
print(result)