def pentagon_nums(n: int):
    nums = {}
    for i in range(1, n+1):
        nums[int((i*((3*i)-1))/2)] = False
    
    return nums

pentagon_numbers = pentagon_nums(100000)

d = 9999999999999999

for i in pentagon_numbers:
    for j in pentagon_numbers:
        if i + j not in pentagon_numbers:
            continue
        absolute = abs(j-i)
        if absolute not in pentagon_numbers:
            continue
        if absolute < d:
            d = absolute
            print(d)

print(d)