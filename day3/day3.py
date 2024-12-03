import re
import math

def extract_mul_instructions(data):
    return re.findall(r"mul\([0-9]+\,[0-9]+\)", data)

def extract_param(mul_instruction):
    param = re.findall(r"[0-9]+", mul_instruction)
    return [int(item) for item in param]


if __name__ == '__main__':
    f = open("day3/data", "r")
    data = f.read()
    mul_instructions = extract_mul_instructions(data)
    answer1 = 0

    for mul_instruction in mul_instructions:
        mul_param = extract_param(mul_instruction)
        answer1 = answer1 + math.prod(mul_param)

    print(f"Solution for first part is {answer1}")
