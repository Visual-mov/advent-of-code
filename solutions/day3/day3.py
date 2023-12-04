import sys

text = open(sys.argv[1]).readlines()
symbols = ['*', '$', '/', '+', '-', '=', '&', '#', '@', '%']
str_nums = [str(n) for n in range(0, 10)]

def get_neighbors(y, x, match):
    if y > 0 and text[y-1][x] in match:
        yield [y-1, x]
    if y < len(text)-1 and text[y+1][x] in match:
        yield [y+1, x]
    if x > 0:
        if text[y][x-1] in match:
            yield [y, x-1]
        if y > 0 and text[y-1][x-1] in match:
            yield [y-1, x-1]
        if y < len(text)-1 and text[y+1][x-1] in match:
            yield [y+1, x-1]
    if x < len(text[y])-1:
        if text[y][x+1] in match:
            yield [y, x+1]
        if y > 0 and text[y-1][x+1] in match:
            yield [y-1, x+1]
        if y < len(text)-1 and text[y+1][x+1] in match:
            yield [y+1, x+1]

def scan_num(y, x):
    if x > 0 and text[y][x-1].isnumeric():
        return scan_num(y, x-1)
    else:
        num = ""
        while text[y][x].isnumeric():
            num += text[y][x]
            x += 1
        return num

# Part one:
total = 0

for y in range(len(text)):
    for x in range(len(text[y])):
        if text[y][x] in symbols:
            nums = []
            for neighbor in get_neighbors(y, x, str_nums):
                n = int(scan_num(neighbor[0], neighbor[1]))
                if not n in nums:
                    nums.append(n)
            total += sum(nums)

print("Part one:", total)

# Part two:
total = 0

for y in range(len(text)):
    for x in range(len(text[y])):
         if text[y][x] == '*':
            nums = []
            for neighbor in get_neighbors(y, x, str_nums):
                n = int(scan_num(neighbor[0], neighbor[1]))
                if not n in nums:
                    nums.append(n)
            if len(nums) == 2:
                total += nums[0] * nums[1]

print("Part two:", total)