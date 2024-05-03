OFFSET = 1000
SIZE = 2001

A = [
    [0 for _ in range(SIZE)]
    for _ in range (SIZE)
]

#직사각형을 입력받고, color로 표시하는 함수
def write_color(color):
    #x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = map(lambda x: int(x)+OFFSET, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            A[x][y] = color
write_color(1) # A
write_color(2) # B
write_color(3) # C

result = 0
for row in A:
    for elem in row:
        if elem in (1,2):
            result += 1
print(result)