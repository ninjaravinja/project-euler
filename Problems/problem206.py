import re
from math import sqrt

min_num = int("1_2_3_4_5_6_7_8_9_0".replace("_", "0"))
max_num = int("1_2_3_4_5_6_7_8_9_0".replace("_", "9"))

minimum = round(sqrt(min_num))
maximum = round(sqrt(max_num)) + 1

for i in range(minimum, maximum) :
    if re.match("1.2.3.4.5.6.7.8.9.0", str(i**2)):
        print(i, i**2)
        break