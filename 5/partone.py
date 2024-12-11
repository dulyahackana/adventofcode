with open("input", "r") as f:
    rules = {}
    lines = []
    for l in f.readlines():
        l = l.strip()
        if l and "|" in l:
            rules[l] = ""
            continue
        if l:
            lines.append(l.split(","))
    right_order_lines = []
    for line in lines:
        to_add = True
        for i, n in enumerate(line[:-1]):
            if line[i] + "|" + line[i+1] not in rules:
                to_add = False
        if to_add:
            right_order_lines.append(line)
    sum = 0
    for line in right_order_lines:
        sum += int(line[int(len(line) / 2)])
    print(sum)