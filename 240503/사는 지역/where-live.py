class People:
    def __init__(self,name,addr,city):
        self.name = name
        self.addr = addr
        self.city = city        
    def info(self):
        print(f"name {self.name}")
        print(f"addr {self.addr}")
        print(f"city {self.city}")

n = int(input())

arr = []
for _ in range(n):
    name, addr, city = tuple(input().split())
    arr.append(People(name,addr,city))

arr.sort(key=lambda p : p.name)

arr[n-1].info()