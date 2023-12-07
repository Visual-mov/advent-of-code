import sys, re, math

text = open(sys.argv[1]).readlines()

(times, dists) = (re.split("\s+", text[0])[1:-1], re.split("\s+", text[1].strip())[1::])
races = [[int(times[i]), int(dists[i]), 0] for i in range(len(times))]

# part 1
for r in races:
    for i in range(r[0]):
        if i * (r[0]-i) > r[1]:
            r[2] += 1

print("Part one:", math.prod([r[2] for r in races]))

# part 2
time = int("".join(times))
dist = int("".join(dists))
victories = 0

for i in range(time):
    if i * (time-i) > dist:
        victories += 1

print("Part two:", victories)