class Agent:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score


agents = []
for _ in range(5):
    code_name, score = input().split()
    agents.append(Agent(code_name, int(score)))

min_idx = 0
for i in range(1, 5):
    if agents[i].score < agents[min_idx].score:
        min_idx = i

print(agents[min_idx].code_name, agents[min_idx].score)