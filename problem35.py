def is_prime(n:int) -> bool:
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    
    return True

count = 0
upper_limit = 1_000_000

for i in range(2, upper_limit+1):
    if i%1000 == 0:
        print(f"\r{i}/{upper_limit} --> {i/upper_limit:.1%}", end="", flush=True)
    number = str(i)
    nums = []
    nums.append(number)
    for j in range(len(number)-1):
        nums.append(nums[j][1:] + nums[j][0])

    if all(is_prime(int(k)) for k in nums):
        count += 1

print(f"\n{count}")