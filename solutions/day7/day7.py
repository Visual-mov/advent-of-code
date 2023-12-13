import sys

text = open(sys.argv[1]).readlines()
hands = [line.strip().split(' ') for line in text]

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

card_map = {}
for i in range(0, len(cards)):
    card_map[cards[i]] = i

def hand_type(hand):
    counts = {}
    for c in hand:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    counts = sorted(counts.values(), reverse=True)
    if counts[0] == 5: return 6
    if counts[0] == 4: return 5
    if counts[0] == 3: return 4 if len(counts) == 2 else 3
    if counts[0] == 2: return 2 if counts[1] == 2 else 1
    return 0

for h in hands:
    h.append(hand_type(h[0]))
hands.sort(key=lambda h: h[2])

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
print("Part one:", winnings)