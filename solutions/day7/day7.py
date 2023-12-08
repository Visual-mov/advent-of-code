import sys

text = open(sys.argv[1]).readlines()
hands = [line.strip().split(' ') for line in text]

card_chars = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards = {}
for i in range(len(card_chars)-1, -1, -1):
    cards[card_chars[i]] = len(card_chars) - i

def hand_typerator(h):
    occurs = {}
    for char in h[0]:
        if char not in occurs:
            occurs[char] = 0
        occurs[char] += 1
    occurs = dict(sorted(occurs.items(), key=lambda item: item[1]))
    print(occurs)

hand_typerator(hands[0])

for h in hands:
    pass