N, B = tuple(map(int,input().split()))
digits = []

while True:
    if N < B:
        digits.append(N)
        break
    digits.append(N % B)
    N //= B

for digit in digits[::-1]:
    print(digit, end="")


# N,B = tuple(map(int,input().split()))

# def convert(N, B):
#     result = ''
#     while N > 0:
#         remain = N % B
#         result = str(remain) + result
#         N //= B
#     return result

# print(convert(N,B))