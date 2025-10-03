nums = {
    0: "SOMETHING GONE WRONG PLS FIX",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred and",
    1000: "one thousand"
}

sum = 0

def length_of_num(i:int):
    if len(str(i)) == 3:
        if int(str(i)[1:]) < 20:
            if int(str(i)[1]) == 0 and int(str(i)[2]) == 0:
                return f"{nums[int(str(i)[0])]} hundred"
            elif int(str(i)[1]) == 0:
                return str(nums[int(str(i)[0])] + " " + nums[100] + " " + nums[int(str(i)[2])])
            else:
                return str(nums[int(str(i)[0])] + " " + nums[100] + " " + nums[int(str(i)[1:])])
        elif int(str(i)[1]) != 0 and int(str(i)[2]) == 0:
            return str(nums[int(str(i)[0])] + " " + nums[100] + " " + nums[int(str(i)[1:])])
        else:
            return str(nums[int(str(i)[0])] + " " + nums[100] + " " + nums[int(f"{str(i)[1]}0")] + " " + nums[int(str(i)[2])])
    elif len(str(i)) == 2:
        if i <= 20:
            return nums[int(str(i))]
        elif i%10 == 0:
            return nums[int(f"{str(i)[0]}0")]
        else:
            return str(nums[int(f"{str(i)[0]}0")] + " " + nums[int(str(i)[1])])
    elif len(str(i)) == 1:
        return nums[int(str(i)[0])]
    elif len(str(i)) == 4:
        return nums[1000]

for i in range(1, 1001):
    length = length_of_num(i)
    sum += len(str(length).replace(" ", ""))
    # print(length)

print(sum)