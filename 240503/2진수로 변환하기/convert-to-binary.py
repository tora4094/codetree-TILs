n = int(input())

if n <= 0:
    print(0)
else:
    digits = []
    while n > 0:
        digits.append(n%2)
        n = n // 2
    print(*digits[::-1],sep="")

# n = 29
# digits = []
# while n > 0:
#     digits.append(n%2)
#     n = n // 2

# print(*digits[::-1], sep="")