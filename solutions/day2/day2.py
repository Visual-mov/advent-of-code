import sys, math

text = open(sys.argv[1]).readlines()
valid_sum = 0
power_sum = 0
totals = {"red": 12, "green": 13, "blue": 14}

for line in text:
    # I'm too lazy to figure out regex
    (game, sets) = line.split(':')
    game = int(game.replace("Game ", ''))
    sets = [s.strip() for s in sets.split(';')]

    valid = True
    fewest = {"red": 0, "green": 0, "blue": 0}
    
    for s in sets:
        counts = [cube.strip().split(' ') for cube in s.split(',')]
        for c in counts:
            (n, color) = (int(c[0]), c[1])
            if n > totals[color]:
                valid = False
            if n > fewest[color]:
                fewest[color] = n

    valid_sum += game if valid else 0
    power_sum += math.prod(fewest.values())

print("Part one:", valid_sum)
print("Part two:", power_sum)
