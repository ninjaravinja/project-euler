def triangle_nums(n: int):
    nums = {}
    for i in range(n):
        nums[int((1/2)*i*(i+1))] = False
    return nums


file = open("./files/0042_words.txt", "r")
lines = []
for line in file:
    words = line.replace("\"", "").split(",")

triangles = triangle_nums(256)
count = 0

for word in words:
    sum = 0
    for letter in word:
        sum += ord(letter)-64
    if sum in triangles:
        count += 1

print(count)