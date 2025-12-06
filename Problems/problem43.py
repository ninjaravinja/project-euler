import itertools

permutations = itertools.permutations(("0","1","2","3","4","5","6","7","8","9"))

count = 0

for perm in permutations:
    perm = ''.join(perm)
    if int(perm[1:4]) % 2 == 0:
        if int(perm[2:5]) % 3 == 0:
            if int(perm[3:6]) % 5 == 0:
                if int(perm[4:7]) % 7 == 0:
                    if int(perm[5:8]) % 11 == 0:
                        if int(perm[6:9]) % 13 == 0:
                            if int(perm[7:10]) % 17 == 0:
                                count += int(perm)

print(count)