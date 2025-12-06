def check_palindrome(num: str) -> bool:
    if num != num[::-1]:
        return False
    
    return True

def lychrel(num: int) -> bool:
    for _ in range(51):
        num += int(str(num)[::-1])
        if check_palindrome(str(num)):
            return False
    
    return True

total = 0

for i in range(10000):
    if lychrel(i):
        total += 1

print(total)

