def repeating_part(numerator: int = 1, denominator: int = 1) -> str:
    seen_remainders = {}
    remainder = numerator % denominator
    decimal = ""
    
    while remainder != 0:
        if remainder in seen_remainders:
            index = seen_remainders[remainder]
            return decimal[index:]
        
        seen_remainders[remainder] = len(decimal)
        remainder *= 10
        decimal += str(remainder // denominator)
        remainder %= denominator
    
    return None


length = 0
num = 0

for i in range(1,1000):
    result = repeating_part(denominator=i)
    if result == None:
        pass
    else:
        result = len(result)
        if result > length:
            length = result
            num = i

print(f"{num = }, {length = }")