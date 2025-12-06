def hcf(num1: int, num2: int) -> int:
    if num1 == num2:
        return num1
    elif num1 < num2:
        for i in range(num1, 0, -1):
            if num1%i == 0 and num2%i == 0:
                return i
    else:
        for i in range(num1, 0, -1):
            if num1%i == 0 and num2%i == 0:
                return i
    
    return -1


nums = []

for i in range(11, 100):
    for j in range(11, 100):
        if str(i).find("0") != -1 or str(j).find("0") != -1:
            pass
        elif i == j:
            pass
        else:
            temp_i = i
            temp_j = j
            for k in range(1,10):
                if str(i).find(str(k)) == -1 or str(j).find(str(k)) == -1:
                    pass
                else:
                    temp_i = i
                    temp_j = j
                    temp_i = str(temp_i).replace(str(k), "", 1)
                    temp_j = str(temp_j).replace(str(k), "", 1)
                
                    if i/j == int(temp_i)/int(temp_j) and int(temp_i)/int(temp_j) < 1:
                        nums.append(f"{int(temp_i)}/{int(temp_j)}")

# simplify any fractions with a hcf
print(nums)
for i in range(len(nums)):
    factor = hcf(int(nums[i].split("/")[0]), int(nums[i].split("/")[1]))
    nums[i] = f"{str(int(int(nums[i].split("/")[0])/factor))}/{str(int(int(nums[i].split("/")[1])/factor))}"

print(nums)

numerator = 1
denominator = 1

for i in range(len(nums)):
    numerator *= int(nums[i].split("/")[0])
    denominator *= int(nums[i].split("/")[1])

new_factor = hcf(numerator, denominator)
print(f"{int(numerator/new_factor)}/{int(denominator/new_factor)}")