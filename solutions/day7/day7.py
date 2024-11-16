import sys

text = open(sys.argv[1]).readlines()
hands = [line.strip().split(' ') for line in text]

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_map = {} # comprehension
for i in range(0, len(cards)):
    card_map[cards[i]] = i

def hand_type(hand, joker=False):
    counts = {}
    for c in hand:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    counts = [list(c) for c in sorted(counts.items(), key=lambda c: c[1], reverse=True)]
    if joker:
        for c in counts:
            if c[0] == "J":
                counts[0][1] += c[1]
    counts = [c[1] for c in counts]


    if counts[0] == 5: return 6
    if counts[0] == 4: return 5
    if counts[0] == 3: return 4 if len(counts) == 2 else 3
    if counts[0] == 2: return 2 if counts[1] == 2 else 1
    return 0

def sort_hands():
    swap = True
    while swap:
        swap = False
        for i in range(len(hands)-1):
            (h1, h2) = (hands[i], hands[i+1])
            if h1[2] == h2[2]:
                for j in range(len(h1[0])):
                    if card_map[h1[0][j]] > card_map[h2[0][j]]:
                        t = hands[i]
                        hands[i] = hands[i+1]
                        hands[i+1] = t
                        swap = True
                        break
                    elif h1[0][j] != h2[0][j]:
                        break

    winnings = 0
    for i in range(len(hands)):
        winnings += (i+1) * int(hands[i][1])
    return winnings

# part one:
for h in hands:
    h.append(hand_type(h[0]))
hands.sort(key=lambda h: h[2])

print("Part one:", sort_hands())

# part two:
cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
card_map = {}
for i in range(0, len(cards)):
    card_map[cards[i]] = i

for h in hands:
    h[2] = hand_type(h[0], True)
hands.sort(key=lambda h: h[2])
print(hands)
print("Part two:", sort_hands())