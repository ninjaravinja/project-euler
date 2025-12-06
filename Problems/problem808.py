from itertools import count
from math import sqrt

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0:
            return False
    
    return True

def is_prime_square(n) -> bool:
    root = int(sqrt(n))
    return root*root == n and is_prime(root)

def palindromic(n: int) -> bool:
    return int(str(n)) == int(str(n)[::-1])

found_squares = set()

for i in count(1):
    if len(found_squares) == 50:
        break
    if is_prime(i):
        squared = i**2
        if not palindromic(squared):
            reverse_squared = int(str(squared)[::-1])
            if is_prime_square(reverse_squared):
                found_squares.add(reverse_squared)
                print(f"Found: {len(found_squares)} - {squared}, {i}, {is_prime(i)}")

print(sum(found_squares))