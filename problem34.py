import math

# calculating upper bound
digits = 0
while True:
    maximum = digits*math.factorial(9)
    if digits < len(str(maximum)):
        digits += 1
    else:
        upper_bound = maximum
        break

factorials = {}
for i in range(0, 10):
    factorials[i] = math.factorial(i)

lower_bound = 10

total = 0

for i in range(lower_bound, upper_bound):
    if i == sum(factorials[int(j)] for j in str(i)):
        total += i

print(total)