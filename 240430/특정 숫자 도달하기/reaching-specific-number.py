arr = list(map(int,input().split()))
new_arr = []
for elem in arr:
    if elem < 250:
        new_arr.append(elem)
    else:        
        break
total = 0
avg = 0
for elem in new_arr:
    total += elem
avg = float(total) / len(new_arr)
print(f"{total} {avg}")