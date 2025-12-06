def eratosthenes(n: int):
    sieve = {i: True for i in range(2, n)}
    for  i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    
    return {i: True for i, v in sieve.items() if v}

count = 0

valid = 0

sieve = eratosthenes(1000000)

for i in sieve:
    if i == 2 or i == 3 or i == 5 or i == 7:
        continue
    valid = 1
    temp1=str(i)
    temp2=str(i)
    for j in range(len(str(i))-1):
        temp1 = temp1[1:]
        temp2 = temp2[:-1]
        
        if temp1 == "" or temp2 == "":
            continue
        # print(i, j, temp1, int(temp2))
        if not (int(temp1) in sieve and int(temp2) in sieve):
            valid = 0

    if valid:
        print(i)
        count += i

print(count)