import sys, re, math

text = open(sys.argv[1]).readlines()

turns = text[0].strip()
graph = {}
for line in text[2::]:
    n = re.findall(r"(\w+)[ =]", line)[0]
    edges = re.findall(r"[\( ](\w+)[,\)]", line)
    graph[n] = edges

# part 1
steps = 0
s = "AAA"

while s != "ZZZ":
    s = graph[s][0 if turns[steps % len(turns)] == "L" else 1]
    steps += 1
print("Part one:", steps)

# part 2
nodes = [n for n in graph.keys() if n[2] == "A"]
steps = 0
counts = []

for i in range(len(nodes)):
    while nodes[i][2] != 'Z':
        nodes[i] = graph[nodes[i]][0 if turns[steps % len(turns)] == "L" else 1]
        steps += 1
    counts.append(steps)
    steps = 0

# find least common multiple of step counts for all starting nodes 
lcm = 1
for n in counts:
    lcm = int(lcm*n / math.gcd(lcm, n))
    
print("Part two:", lcm)