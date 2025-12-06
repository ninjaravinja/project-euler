highest = 0

for a in range(1, 101):
    for b in range(1, 101):
        total = sum(int(i) for i in str(a**b))
        if total > highest:
            highest = total

print(highest)