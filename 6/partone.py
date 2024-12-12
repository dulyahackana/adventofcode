def dirs():
    while True:
        _dirs = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]
        for d in _dirs:
            yield d

def get_next_dir(d=0):
    d += 1
    if d == len(dirs):
        d = 0
    return dirs[d]

with open("input", "r") as f:
    m = []
    for l in f.readlines():
        m.append(l.strip())
    dir_gen = dirs()
    d = next(dir_gen)
    size = len(m)
    for i, l in enumerate(m):
        for j, p in enumerate(l):
            if p == "^":
                x = i; y = j
    steps = {
        "%d|%d" % (x, y): ""
    }
    while True:
        x1 = x + d[0]; y1 = y + d[1]
        if x1 < 0 or x1 > size - 1 or y1 < 0 or y1 > size - 1:
            break
        if m[x1][y1] not in [".", "^"]:
            d = next(dir_gen)
            continue
        x = x1; y = y1
        steps["%d|%d" % (x, y)] = ""
    print(len(steps.keys()))
