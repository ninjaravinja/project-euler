count = 0

for i in range(1,10):
    if i % 1000000 == 0:
        print(f"Current i: {i}")
    for j in range(1,22):
        if len(str(i**j)) > j:
            break
        if len(str(i**j)) == j:
            print(i, j, i**j)
            count += 1

print(count)