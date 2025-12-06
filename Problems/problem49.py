from itertools import permutations
from math import sqrt

def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    
    return True

temp = []

found = {}

limit = 1_000
length = 4

for i in range(limit, limit*10):
    if not is_prime(i):
        continue
    if i in found:
        continue
    
    temp = list(set([int(''.join(perm)) for perm in permutations(str(i))]))
    # temp.sort()
    # print(temp)
    
    if any(i in found[j] for j in found):
        continue
    
    for j in range(len(temp)):
        if len(str(temp[j])) < length:
            continue
        for k in range(j, len(temp)):
            diff = temp[k] - temp[j]
            if diff <= 0:
                continue
            if temp[j] + diff in temp and temp[k] + diff in temp:
                if is_prime(temp[j]) and is_prime(temp[k]) and is_prime(temp[j] + (2*diff)):
                    result = [str(temp[j]), str(temp[k]), str(temp[j] + (2*diff))]
                    found[','.join(result)] = result
                    break

for i in found:
    print(''.join(i).replace(",", ""))