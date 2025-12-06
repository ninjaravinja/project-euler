from itertools import permutations

count = 1

for perm in permutations("0123456789"):
    if count == 1_000_000:
        print(int(''.join(perm)))
        break
    count += 1