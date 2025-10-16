from math import sqrt

perimeter = 1000

temp = {i: [0,[]] for i in range(1, perimeter + 1)}

for p in range(1, perimeter + 1):
    print(f"{p = }")
    for i in range(1,p+1):
        for j in range(1, p-i+1):
            k = sqrt(i**2 + j**2)
            if not k.is_integer():
                continue
            if i+j+k > p:
                break
            if i+j+k != p:
                continue
            if i**2 + j**2 != k**2:
                continue
            if i in temp[p][1] or j in temp[p][1] or k in temp[p][1]:
                continue
            temp[p][0] = temp[p][0] + 1
            temp[p][1].append(i)

num = sorted(temp, key=temp.get, reverse=True)[0]
print(f"{num}: {temp[num][0]}")