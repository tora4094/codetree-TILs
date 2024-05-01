arr = list(map(int,input().split()))
new_arr = []
for elem in arr:
    if (elem == 0):
        break
    if (elem % 2 == 0):
        new_arr.append(int(elem / 2))
    else:
        new_arr.append(elem + 3)
for elem in new_arr:
    print(elem,end=" ")