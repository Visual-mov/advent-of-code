import sys

text = open(sys.argv[1]).readlines()

def get_next(seq: list) -> int:
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    return seq[-1] if all(n == 0 for n in diffs) else seq[-1] + get_next(diffs)

total = 0
for line in text:
    seq = [int(n) for n in line.strip().split(' ')]
    total += get_next(seq)
print("Part one", total)