class People:
    def __init__(self,name,h,w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())
arr = []
for _ in range(n):
    name, h, w = tuple(input().split())
    arr.append(People(name,int(h),int(w)))

arr.sort(key=lambda p : (p.h,-p.w))

for p in arr:
    print(p.name,p.h,p.w)