from itertools import count
from math import sqrt

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n <= 1 or n%2 == 0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0:
            return False
    
    return True

step = 2
num = [1]
primes = []
ratio = 1

while ratio > 0.1:
    for _ in range(4):
        temp = num[-1] + step
        num.append(temp)
        if is_prime(temp):
            primes.append(temp)
    step+=2
    ratio = len(primes)/len(num)

print(num[-1] - num[-2] + 1)