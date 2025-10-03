def sum_of_divisors(num: int) -> int:
    sum = 0
    for i in range(1,int((num/2)+1)):
        if num%i == 0:
            sum += i
    
    return sum

sum = 0
for i in range(10_001):
    if i == sum_of_divisors(sum_of_divisors(i)) and i != sum_of_divisors(i):
        print(i, sum_of_divisors(i))
        sum += i

print(sum)