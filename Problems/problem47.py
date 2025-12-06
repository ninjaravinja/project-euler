def eratosthenes(n: int) -> dict[int, bool]:
    sieve = {i: True for i in range(2, n)}
    for  i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    
    return {i: True for i, v in sieve.items() if v}

def prime_factors(n: int, seive: dict[int, bool]) -> dict[int, bool]:
    factors = {}
    
    for i in range(2, (n//2)+1):
        if n%i == 0 and i in seive:
            factors[i] = True
    
    return factors

limit = 4

seive = eratosthenes(100000)
nums = [0 for _ in range(limit)]

counter = -1

while any(i == 0 for i in nums):
    counter += 1
    if counter % 10000 == 0:
        print(f"Current {counter = }")
    factors = []
    for i in range(limit):
        factors.append(prime_factors(counter+i, seive))
    if any(len(x) < limit for x in factors):
        continue
    for i in range(limit):
        nums[i] = counter+i

print(nums)