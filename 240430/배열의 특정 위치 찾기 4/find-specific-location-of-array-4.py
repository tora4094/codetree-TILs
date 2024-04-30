arr = list(map(int,input().split()))
count = 0
total = 0
for elem in arr:
    if elem != 0: 
        if elem % 2 == 0:
            count += 1
            total += elem        
    else:
        break
print(f"{count} {total}")