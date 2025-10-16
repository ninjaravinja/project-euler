fractional_part = []

for i in range(1,1_000_000):
    fractional_part += str(i)

nums = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]

product = 1

for i in nums:
    product *= int(fractional_part[i-1])

print(product)