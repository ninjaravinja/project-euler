target = 100

array = [0] * (target + 1)
array[0] = 1

for i in range(1, target):
    for j in range(i, target + 1):
        array[j] += array[j - i]

print(array[target])