class agent:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
arr = list(input().split())
agent1 = agent(arr[0],arr[1],arr[2])
print(f"secret code : {agent1.secret_code}")
print(f"meeting point : {agent1.meeting_point}")
print(f"time : {agent1.time}")