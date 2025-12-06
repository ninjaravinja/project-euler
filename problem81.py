with open('./files/0081_matrix.txt', 'r') as f:
    matrix: list = f.readlines()

for i in range(len(matrix)):
    matrix[i] = [int(j) for j in matrix[i].split(",")]

min_path = []

for i in range(len(matrix)):
    min_path.append([0] * len(matrix))

for i in range(len(matrix)):
    min_path[i][0] = sum([matrix[j][0] for j in range(i+1)])
    min_path[0][i] = sum(matrix[0][:i+1])


for i in range(1, len(matrix)):
    for j in range(1, len(matrix)):
        min_path[i][j] = min(min_path[i][j-1], min_path[i-1][j]) + matrix[i][j]


print(min_path[-1][-1])