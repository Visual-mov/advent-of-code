import sys

text = open(sys.argv[1]).readlines()
text = [l.strip() for l in text]

# width = len(text.split('\n')[0])
# height = len(text)//width

ori = {
    "|": "NS", "-": "WE",
    "L": "NE", "J": "NW",
    "7": "SW", "F": "SE",
}

def get_tile(pos):
    return text[pos[0]][pos[1]]

def connected(t1, t2, pos):
    if pos[0] == 1:
        

def build_graph(pos, sp=None, graph=[]):
    pt = get_tile(pos)
    if sp == None:      # init starting point
        sp = pos
    if pt == get_tile(sp):   # end condition
        return graph
    print(pt)
    for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]:    # go through neighbors
        n = (pos[0]+i[0], pos[1]+i[1])
        nt = get_tile(n)
        d = ori[nt]

        if (n[0] < 0 or n[1] < 0) or (n[0] > len(text[0])-1 or n[1] > len(text)-1):
            continue
        
        if ori[get_tile(pos)][1] == d[0]:
            if get_tile(n) == "-":
                graph.append([get_tile(n), d])
            return build_graph(n, sp, graph)

for i in range(len(text)-1):
    for j in range(len(text[0])-1):
        if text[i][j] == "S":
            g = build_graph((i, j))
            print(g)
            exit()

# build loop nodes

# assign distances, explore both path directions and pick one that reaches start first use that distance

