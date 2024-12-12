def get_next_dir(d=[1,0]):
    if d == [-1, 0]:
        return [0, 1]
    if d == [0, 1]:
        return [1, 0]
    if d == [1, 0]:
        return [0, -1]
    if d == [0, -1]:
        return [-1, 0]

with open("input", "r") as f:
    m = []
    for l in f.readlines():
        m.append(l.strip())
    d = [-1, 0]
    size = len(m)
    for i, l in enumerate(m):
        for j, p in enumerate(l):
            if p == "^":
                x = i; y = j
    steps = {
        "%d|%d" % (x, y): [d]
    }
    while True:
        x1 = x + d[0]; y1 = y + d[1]
        if x1 < 0 or x1 > size - 1 or y1 < 0 or y1 > size - 1:
            break
        if m[x1][y1] not in [".", "^"]:
            d = get_next_dir(d)
            continue
        else:
            
        x = x1; y = y1
        if "%d|%d" % (x, y) in steps.keys():
            steps["%d|%d" % (x, y)].append(d)
        else:
            steps["%d|%d" % (x, y)] = [d]
    print(steps)

