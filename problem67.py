triangle = []

file = open("./0067_triangle.txt", "r")

for line in file:
    triangle.append(line.split("\n")[0])



map = []
for i in triangle:
    map.append(i.split(" "))

for i in range(len(map)):
    for j in range(i+1):
        map[i][j] = int(map[i][j])



while len(map) != 1:
    new_map = []
    for i in range(len(map)-2):
        new_map.append(map[i])
    
    temp = []
    for i in range(len(map[-1])-1):
        if map[-1][i] + map[-2][i] < map[-1][i+1] + map[-2][i]:
            temp.append(map[-1][i+1] + map[-2][i])
        else:
            temp.append(map[-1][i] + map[-2][i])

    new_map.append(temp)
    
    map = new_map

print(map)