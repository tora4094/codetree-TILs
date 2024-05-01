n = int(input())
arr = [1,n]
for i in range (2, 10):
    a = arr[i - 2] + arr [i - 1]
    arr.append(a)
    if (a >= 100):
        break
for elem in arr:
    print(elem,end=" ")