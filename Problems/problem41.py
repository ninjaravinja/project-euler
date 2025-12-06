import itertools
from math import sqrt

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    
    return True

num = 0
limit = 9

for i in range(1, limit+1):
    digits = [str(i) for i in range(1, i+1)]
    print(digits)
    
    permutations = itertools.permutations(digits)

    for perm in permutations:
        perm = ''.join(perm)
        if is_prime(int(perm)):
            print(int(perm))
            num = int(perm)

print(num)