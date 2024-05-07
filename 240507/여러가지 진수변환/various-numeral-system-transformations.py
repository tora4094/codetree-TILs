N,B = tuple(map(int,input().split()))

def convert(N, B):
    result = ''
    while N > 0:
        remain = N % B
        result = str(remain) + result
        N //= B
    return result

print(convert(N,B))