n = int(input())
count = 0
for _ in range(0, n):
    arr = list(map(int,input().split()))
    avg = sum(arr) / 4.0
    if avg >= 60:
        print("pass")
        count += 1
    else:
        print("fail")
print(count)