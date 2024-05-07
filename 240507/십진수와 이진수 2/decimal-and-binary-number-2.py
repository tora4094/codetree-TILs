arr = list(map(int, list(input())))
length = len(arr)

num = 0
for i in range(length):
    num = num * 2 + arr[i]
num *= 17

new_arr = []
while True:
    if num < 2:
        new_arr.append(num)
        break;
    new_arr.append(num % 2)
    num //= 2

for elem in new_arr[::-1]:
    print(elem,end="")