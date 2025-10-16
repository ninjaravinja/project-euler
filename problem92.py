seen_89s = {89: True}
count = 0

for i in range(1, 10_000_000):
    if i == 1:
        continue
    if i == 89:
        count += 1
        continue
    new_num = int(sum(int(j)**2 for j in str(i)))
    while new_num != 89 and new_num != 1:
        new_num = int(sum(int(j)**2 for j in str(new_num)))
    if new_num == 89:
        count += 1
        continue
print(count)