import sys

text = open(sys.argv[1]).readlines()

def scan_nums():
    total = 0
    for line in text:
        digits = []
        for c in line:
            if c.isnumeric():
                digits.append(c)
        total += int(digits[0] + digits[len(digits)-1])
    return total

# part one:
print("Part one:", scan_nums())

# part two:
nums = {"one": '1e', "two": '2o', "three": '3e',
        "four": '4', "five": '5e', "six": '6',
        "seven": '7n', "eight": '8t', "nine": '9e'}

for i in range(len(text)):
    tok = ""
    for c in text[i]:
        tok += c
        for digit in nums.keys():
            if tok.find(digit) != -1:
                tok = tok.replace(digit, nums[digit])
        text[i] = tok

print("Part two:", scan_nums())