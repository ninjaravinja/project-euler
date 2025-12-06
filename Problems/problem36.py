# bin(ord("a"))[2:]

sum = 0

for i in range(1, 1_000_001):
    binary = bin(ord(chr(i)))[2:]
    if str(i) == str(i)[::-1] and binary == binary[::-1]:
        print(i, binary)
        sum += i

print(sum)