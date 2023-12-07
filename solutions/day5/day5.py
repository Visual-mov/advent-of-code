import sys

text = open(sys.argv[1]).readlines()
seeds = [int(n) for n in text[0].strip().split(': ')[1].split(' ')]
maps = []

def main():

    r = []
    for line in text:
        if line[0].isnumeric():
            r.append([int(n) for n in line.strip().split(' ')])
        elif r != []:
            maps.append(r)
            r = []
    maps.append(r)

    # part one:
    lowest = get_location(seeds[0])
    for seed in seeds[1::]:
        if (l := get_location(seed)) < lowest:
            lowest = l
    print("Part one:", lowest)

    # part two:
    # ranges = []
    # start = time.time()

    # for i in range(0, len(seeds), 2):
    #     ranges.append((seeds[i], seeds[i+1]))
    #ranges.sort(key=lambda r: r[0])

    # will take 100 million years to finish
    # lowest = get_location(seeds[0])
    # for r in ranges:
    #     for i in range(r[0], r[0]+r[1]):
    #         if (l := get_location(i)) < lowest:
    #             lowest = l
    #     print("Range complete, took %s seconds" % (time.time() - start))

    # print("Part two:", lowest)

def get_location(seed):
    loc = seed
    for m in maps:
        for r in m:
            if loc >= r[1] and loc-r[1] <= r[2]:
                loc = r[0] + loc-r[1]
                break
    return loc

if __name__ == "__main__":
    main()