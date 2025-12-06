num1 = 1
num2 = 1
num3 = 2

index = 2

while len(str(num3)) < 1000:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    index += 1

print(index)