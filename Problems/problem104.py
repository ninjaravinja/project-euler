import math

nums = ["1","2","3","4","5","6","7","8","9"]

flag = False

num1 = 1
num2 = 1
count = 2

while not flag:
    if any(j not in str(num2%(10**9)) for j in nums):
        num1, num2 = num2, num1 + num2
        count += 1
        continue
    elif any(j not in str(num2 // (10**(int(math.log10(num2)-8)))) for j in nums):
        num1, num2 = num2, num1 + num2
        count += 1
        continue
    else:
        break

print(f"{count = }")