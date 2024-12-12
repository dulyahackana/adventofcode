with open("input", "r") as f:
    safe = 0
    for l in f.readlines():
        nums = list(map(int, l.split()))
        if nums == sorted(nums) or nums == sorted(nums, reverse=True):
            s = True
            for i in range(len(nums) - 1):
                diff = abs(nums[i] - nums[i + 1])
                if diff < 1 or diff > 3:
                    s = False
            if s:
                safe += 1
    print(safe)
