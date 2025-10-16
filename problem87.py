from math import floor, sqrt

def eratosthenes(n: int):
    sieve = {i: True for i in range(2, n)}
    for  i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    
    return {i: True for i, v in sieve.items() if v}

limit = floor(sqrt(50_000_000))
nums = eratosthenes(limit)
found_nums = {}

for i in nums:
    for j in nums:
        for k in nums:
            sum = i**2 + j**3 + k**4
            if sum < 50_000_000:
                found_nums[sum] = True

print(len(found_nums))