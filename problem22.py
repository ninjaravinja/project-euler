file = open("./files/0022_names.txt", "r")

for line in file:
    line = line.replace("\"", "")

names = line.split(",")

names.sort()

def name_value(name):
    sum = 0
    for letter in name:
        sum += ord(letter)-64
    
    return sum

total = 0

for i in range(len(names)):
    total += (name_value(names[i]) * (i+1))

print(total)