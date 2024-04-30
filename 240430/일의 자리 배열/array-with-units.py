arr = list(map(int,input().split()))
for i in range (2, 10):
    new_elem = (arr[i-2] + arr[i-1])
    arr.append(new_elem % 10)

for i in arr:
    print(f"{i}",end=" ")