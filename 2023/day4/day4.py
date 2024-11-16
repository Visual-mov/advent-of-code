import sys, re

text = open(sys.argv[1]).readlines()

def get_card(line):
    (winning, nums) = line.split(':')[1].split('|')
    return {"winning": re.split("\s+", winning.strip()), "nums": re.split("\s+", nums.strip())}

cards = [get_card(line) for line in text]

# Part one:
points = 0

for card in cards:
    value = 0
    for n in card["nums"]:
        if n in card["winning"]:
            value = (value * 2) if value != 0 else 1
    points += value

print("Part one:", points)

# Part two:
count = 0
copies = [1 for i in range(len(cards))]

for i in range(len(cards)):
    matching = sum([1 if n in cards[i]["winning"] else 0 for n in cards[i]["nums"]])
    for j in range(1, matching+1):
        copies[i+j] += copies[i]
    count += copies[i]

print("Part two:", count)