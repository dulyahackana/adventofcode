def is_safe(nums):
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        s = True
        for i in range(len(nums) - 1):
            diff = abs(nums[i] - nums[i + 1])
            if diff < 1 or diff > 3:
                s = False
        if s:
            return True
    return False

with open("input", "r") as f:
    safe = 0
    for l in f.readlines():
        onums = list(map(int, l.split()))
        s = False
        for j in range(len(onums)):
            nums = onums.copy()
            nums.pop(j)
            if is_safe(nums):
                s = True
                break
        if s:
            safe += 1
    print(safe)
