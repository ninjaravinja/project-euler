target = 1000

last_ten = 0

for i in range(1, target+1):
    temp = i
    for j in range(1, i):
        temp *= i
    last_ten += int(str(temp)[-10:])
    last_ten = int(str(last_ten)[-10:])

print(str(last_ten).zfill(10))

# OR THIS

print(str(sum(i**i for i in range(1, 1001)))[-10:])