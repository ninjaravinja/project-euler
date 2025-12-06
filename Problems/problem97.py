# print(str(28433 * 2**7830457 + 1)[-10:])

num = 1

for i in range(7830457):
    num = int(str(2*num)[-10:])

print(str(28433 * num + 1)[-10:])