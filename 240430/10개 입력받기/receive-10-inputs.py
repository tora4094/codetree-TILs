arr = list(map(int,input().split()))

new_arr = []
for elem in arr:
    if (elem != 0):
        new_arr.append(elem)
    else:
        break

total = sum(new_arr)
avg = float(total) / len(new_arr)

print(f"{total} {avg:.1f}")