import sys, re, math

text = open(sys.argv[1]).readlines()

(times, dists) = (re.split("\s+", text[0])[1:-1], re.split("\s+", text[1].strip())[1::])
races = [[int(times[i]), int(dists[i]), 0] for i in range(len(times))]

for r in races:
    for i in range(r[0]):
        if i * (r[0]-i) > r[1]:
            r[2] += 1

print("Part one:", math.prod([r[2] for r in races]))