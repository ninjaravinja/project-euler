import itertools

nums = "1","2","3","4","5","6","7","8","9"

total = {}

for perm in itertools.permutations(nums):
    perm = ''.join(perm)
    for i in range(1, len(perm)):
        substring1 = perm[:i]
        for j in range(i+1, len(perm)):
            substring2 = perm[i:j]
            substring3 = perm[j:]
            
            substring3 = int(substring3)
            substring2 = int(substring2)
            substring1 = int(substring1)
            
            if int(substring1) * int(substring2) == int(substring3):
                print(f"{substring1} * {substring2} = {substring3}")
                total[int(substring3)] = [substring1,substring2]

print(sum(total.keys()))