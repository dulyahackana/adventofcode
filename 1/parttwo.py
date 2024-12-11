import re

with open("input", "r") as f:
    left = []
    right = []
    sum = 0
    for l in f.readlines():
        nums = l.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    d = {}
    for r in right:
        if r not in d:
            d[r] = 1
        else:
            d[r] += 1
    for l in left:
        if l in d:
            sum += l * d[l]
    print(sum)