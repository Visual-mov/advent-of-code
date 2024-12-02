import sys
text = open(sys.argv[1]).readlines()

l1 = []; l2 = []
for line in text:
    pair = line.split()
    l1.append(int(pair[0]))
    l2.append(int(pair[1]))

l1.sort()
l2.sort()

sum = 0; score = 0
for i in range(len(l1)):    
    n = 0
    for j in range(len(l1)):
        if l1[i] == l2[j]: n += 1
    score += l1[i] * n
    sum += abs(l1[i] - l2[i])

print("Part one:", sum)
print("Part two:", score)