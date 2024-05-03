class Plane2D:
    def __init__(self,x,y,number):
        self.x = x
        self.y = y
        self.number = number
    def mangattan_distance(self):
        return abs(self.x) + abs(self.y)

n = int(input())

arr = []
for i in range(1, n+1):
    x, y = map(int,input().split())
    arr.append(Plane2D(x,y,i))

arr.sort(key=lambda p: (p.mangattan_distance(), p.number))

for p in arr:
    print(p.number)