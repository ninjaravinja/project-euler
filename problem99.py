highest = 0
line_num = 1

sorted_arr = []

with open("./files/0099_base_exp.txt", "r") as f:
    line = f.readline().replace("\n", "").split(",")
    while line != ['']:
        sorted_arr.append([[int(line[0]), int(line[1])], line_num])
        line = f.readline().replace("\n", "").split(",")
        line_num += 1

sorted_arr.sort(key=lambda x: x[0][0]**x[0][1], reverse=True)
print(sorted_arr[0])