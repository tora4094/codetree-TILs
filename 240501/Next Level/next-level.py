class User:
    def __init__(self,id,level=1):
        self.id = id
        self.level = level
    def info(self):
        print(f"user {self.id} lv {self.level}")

id, level = tuple(input().split())
user1 = User("codetree",10)
user2 = User(id,int(level))

user1.info()
user2.info()