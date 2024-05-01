n = int(input())
arr = list(map(int,input().split()))

cnt = {}
for elem in arr:
    if elem in cnt:
        cnt[elem] += 1
    else:
        cnt[elem] = 1

result = -1
for elem in arr:
    if cnt[elem] == 1:
        if elem > result:
            result = elem

print(result)