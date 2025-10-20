def eratosthenes(n: int):
    sieve = {i: True for i in range(2, n)}
    for  i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    
    return {i: True for i, v in sieve.items() if v}

def num_of_factors(n: int) -> int:
    count = 0
    for i in range(1,n):
        if n%i == 0:
            count += 1
    
    return count

def composite_odd_numbers(n: int) -> list[int, bool]:
    nums = {}
    for i in range(1, n+1):
        if num_of_factors(i) >= 2 and i%2 != 0:
            nums[i] = True
    
    return nums

limit = 10000

composites = composite_odd_numbers(limit)

odd_nums = eratosthenes(limit)

found = {}

for i in composites:
    for j in odd_nums:
        for k in range(100):
            if i == j + 2*(k**2) and i not in found:
                found[i] = True

print(found.keys())

for i in composites:
    if i not in found:
        print(i)