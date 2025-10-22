counter = 100_000

found = False

counts = {}

while not found:
    for i in range(100_000, 1_000_000):
        if all(str(i).count(j) == str(i*2).count(j) for j in str(i)):
            if all(str(i).count(j) == str(i*3).count(j) for j in str(i)):
                if all(str(i).count(j) == str(i*4).count(j) for j in str(i)):
                    if all(str(i).count(j) == str(i*5).count(j) for j in str(i)):
                        if all(str(i).count(j) == str(i*6).count(j) for j in str(i)):
                            print([str(i*j) for j in range(1,7)])
                            found = True
                            break
        counter += 1

print(counter)