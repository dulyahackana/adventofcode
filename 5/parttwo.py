from functools import cmp_to_key

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
    not_right_order_lines = []
    for line in lines:
        to_add = True
        for i, n in enumerate(line[:-1]):
            if line[i] + "|" + line[i+1] not in rules:
                to_add = False
        if not to_add:
            not_right_order_lines.append(line)
    def compare(x, y):
        if x + "|" + y in rules:
            return -1
        elif y + "|" + x in rules:
            return 1
        return 0
    sum = 0
    for line in not_right_order_lines:
        print(line)
        line = sorted(line, key=cmp_to_key(compare))
        sum += int(line[int(len(line) / 2)])
    print(sum)