import sys, re

text = open(sys.argv[1]).readlines()

turns = text[0].strip()

graph = {}
for line in text[2::]:
    n = re.findall(r"(\w+)[ =]", line)[0]
    edges = re.findall(r"[\( ](\w+)[,\)]", line)
    graph[n] = edges

# def search_steps(s, t, t_index=0, steps=0):
#     if t_index == len(turns):
#         t_index = 0
#     if s == t:
#         return steps
#     steps += 1
#     turn = turns[t_index]
#     t_index += 1
#     return search_steps(graph[s][0 if turn == "L" else 1], t, t_index, steps)

steps = 0
s = "AAA"
t_index = 0
while s != "ZZZ":
    if t_index == len(turns):
        t_index = 0
    s = graph[s][0 if turns[t_index] == "L" else 1]
    steps += 1
    t_index += 1

print("Part one:", steps)
