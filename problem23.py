def type_of_num(num:int) -> str:
    sum = 0
    for i in range(1,int(num/2)+1):
        if num%i==0:
            sum += i
    
    if sum == num:
        return "perfect"
    elif sum < num:
        return "deficient"
    else:
        return "abundant"


abundant_numbers = [i for i in range(1,28124) if type_of_num(i) == "abundant"]


nums = []

for i in abundant_numbers:
    for j in abundant_numbers:
        temp = i+j
        if temp < 28123:
            nums.append(temp)
        else:
            break


sum = 0

for i in range(1, 28123):
    if i not in nums:
        sum += i

print(sum)

# 4179871