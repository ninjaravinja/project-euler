from fractions import Fraction

counter = 0

frac = 1 + Fraction(1, 2)

for i in range(999):
    frac = 1 + Fraction(1, 1 + frac)
    frac_parts = str(frac).split("/")
    if len(frac_parts[0]) > len(frac_parts[1]):
        counter += 1

print(counter)