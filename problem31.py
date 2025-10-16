coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

array = [0] * (target + 1)
array[0] = 1

for coin in coins:
    for i in range(coin, target + 1):
        array[i] += array[i - coin]

print(array[target])