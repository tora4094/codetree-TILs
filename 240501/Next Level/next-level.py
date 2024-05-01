class User:
    def __init__(self,id="",level=1):
        self.id = id
        self.level = level
    def info(self):
        print(f"user {self.id} lv {self.level}")

user1 = User()
user2 = User()

user1.id = "codetree"
user1.level = 10

id, level = tuple(input().split())

user2.id = id
user2.level = int(level)

user1.info()
user2.info()