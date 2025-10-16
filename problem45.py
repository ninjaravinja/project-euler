def triangle_nums(n: int):
    nums = {}
    for i in range(n):
        nums[int((1/2)*i*(i+1))] = False
    
    return nums

def pentagon_nums(n: int):
    nums = {}
    for i in range(1, n+1):
        nums[int((i*((3*i)-1))/2)] = False
    
    return nums

def hexagon_nums(n: int):
    nums = {}
    for i in range(1, n+1):
        nums[int(i*((2*i)-1))] = False
    
    return nums

limit = 100_000

triangles = triangle_nums(limit)
pentagons = pentagon_nums(limit)
hexagons = hexagon_nums(limit)

for num in triangles:
    if num == 1:
        continue
    if num in pentagons and num in hexagons:
        print(f"Found {num} in pentagons and hexagons")