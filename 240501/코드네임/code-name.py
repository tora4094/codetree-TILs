class Agent:
    def __init__(self,code_name,score=0):
        self.code_name = code_name
        self.score = score

agents = []
for _ in range(5):
    code_name, score = tuple(input().split())
    agents.append(Agent(code_name, int(score)))

min_index = 0

for i in range(1,5):
    if agents[min_index].score > agents[i].score:
        min_index = i

print(agents[min_index].code_name,agents[min_index].score)