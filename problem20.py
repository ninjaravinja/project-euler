num = 100

total = 1

for i in range(1,num):
    total *= i

count = 0

for i in str(total):
    count += int(i)

print(count)