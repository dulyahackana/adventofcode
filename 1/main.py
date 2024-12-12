with open("input", "r") as f:
    left = []
    right = []
    for l in f.readlines():
        nums = l.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    left = sorted(left)
    right = sorted(right)
    d = 0
    for i in range(len(left)):
        d += abs(right[i] - left[i])
    print(d)

if __name__ == "__main__":
    print("Hello World!")