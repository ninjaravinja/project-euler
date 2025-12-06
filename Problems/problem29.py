nums = {}
for a in range(2, 101):
    for b in range(2, 101):
        nums[a**b] = f"{a}**{b}"

print(len(nums))