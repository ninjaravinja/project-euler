def bouncy(n: int) -> bool:
    num = str(n)
    if all(int(num[i]) >= int(num[i+1]) for i in range(len(num)-1)):
        return False
    if all(int(num[i]) <= int(num[i+1]) for i in range(len(num)-1)):
        return False
    
    return True

count = 100
found = 0

while True:
    if bouncy(count):
        found += 1
        if int((found/count)*100) == 99:
            print(count)
            break
        count += 1
    else:
        count += 1

