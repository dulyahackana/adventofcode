import re

with open("input", "r") as f:
    sum = 0
    text = f.read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)

    for match in matches:
        sum += int(match[0]) * int(match[1])
    print(sum)