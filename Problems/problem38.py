nums = "1","2","3","4","5","6","7","8","9"

temp = ""
highest = [0,0]

for i in range(1,1000000):
    temp = ""
    for j in range(1,5):
        if len(temp) >= 9:
            break
        temp += str(i*j)
    if len(temp) > 9:
        continue
    if any(i not in temp for i in nums):
        continue
    if int(temp) > highest[0]:
        highest[0] = int(temp)
        highest[1] = i

print(highest)