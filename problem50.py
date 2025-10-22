def eratosthenes(n: int):
    sieve = {i: True for i in range(2, n)}
    for  i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    
    return {i: True for i, v in sieve.items() if v}

limit = 1_000_000

primes_set = eratosthenes(limit)
primes = list(primes_set)

consecutive = 1

highest = 0
count = 0

prefix = [0]
for p in primes:
    prefix.append(prefix[-1] + p)
print(prefix)

for i in range(len(primes)):
    for j in range(i+count, len(primes)):
        temp = prefix[j] - prefix[i]
        if temp > limit:
            break
        if temp in primes:
            if j-i > count:
                count = j-i
                highest = temp

print(highest, count)