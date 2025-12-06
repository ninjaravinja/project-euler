def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    
    return True

b_nums = [i for i in range(2,1001) if is_prime(i)]

highest_n = 0
product = 0

for b in b_nums:
    for a in range(-999, 1000):
        n = 0
        while is_prime((n*n) + (a*n) + b):
            n += 1
        if n-1 > highest_n:
            highest_n = n-1
            product = a*b
        print(n-1)

print(highest_n, product)
# -59231