import sys

text = open(sys.argv[1]).readlines()

symbols = ['*', '$', '/', '+', '-', '=', '&', '#', '@', '%']
# for line in text:
#     for c in line.strip():
#         if not c.isnumeric() and c != '.' and c not in symbols: 
#             symbols.append(c)

total = 0
num = ""
is_part = False
for y in range(len(text)):
    for x in range(len(text[y])):
        if text[y][x].isnumeric():
            if y > 0 and text[y-1][x] in symbols:
                    is_part = True
            if y < len(text)-1 and text[y+1][x] in symbols:
                    is_part = True
            if x > 0:
                if text[y][x-1] in symbols:
                    is_part = True
                if y > 0 and text[y-1][x-1] in symbols:
                    is_part = True
                if y < len(text)-1 and text[y+1][x-1] in symbols:
                    is_part = True
            if x < len(text[y])-1:
                if text[y][x+1] in symbols:
                    is_part = True
                if y > 0 and text[y-1][x+1] in symbols:
                    is_part = True
                if y < len(text)-1 and text[y+1][x+1] in symbols:
                    is_part = True
            num += text[y][x]
        else:
            if is_part:
                total += int(num)
                is_part = False
            if num != "":
                num = ""

print("Part one:", total)