import re

with open("input", "r") as f:
    sum = 0
    filecontent = f.read()
    text = ""
    while filecontent:
        dont_inx = filecontent.find("don't()")
        if dont_inx == -1:
            text += filecontent
            break
        text += filecontent[:dont_inx]
        filecontent = filecontent[dont_inx+7:]
        do_inx = filecontent.find("do()")
        if do_inx == -1:
            break
        filecontent = filecontent[do_inx+4:]
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)

    for match in matches:
        sum += int(match[0]) * int(match[1])
    print(sum)