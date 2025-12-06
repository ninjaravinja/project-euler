step = 2

end = (2*1001)-1

num = [1]

i = 1

while i < end:
    for _ in range(4):
        # num.append((2*i)-1)
        num.append(num[-1] + step)
        i+=1
    step+=2

print(sum(num))