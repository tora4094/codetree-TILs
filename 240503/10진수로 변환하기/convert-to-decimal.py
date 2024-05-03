arr = list(input())
arr = [int(elem) for elem in arr]

num = 0
for i in range(len(arr)):
    num = num * 2 + arr[i]
print(num)



# binary = [1, 1, 1, 0, 1]
# num = 0

# for i in range(5):
#     num = num * 2 + binary[i]
# print(num)