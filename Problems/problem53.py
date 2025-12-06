import math

count = 0

for i in range(23, 101):
    for j in range(i):
        if math.comb(i,j) > 1_000_000:
            count += 1

print(count)