import re
import math

def extract_mul_instructions(data):
    return re.findall(r"mul\([0-9]+\,[0-9]+\)", data)

def extract_param(mul_instruction):
    param = re.findall(r"[0-9]+", mul_instruction)
    return [int(item) for item in param]

def compute_mul_instructions(mul_instructions):
    result = 0
    for mul_instruction in mul_instructions:
        mul_param = extract_param(mul_instruction)
        result = result + math.prod(mul_param)
    return result

def find_dont(data):
    return re.split(r'don\'t', data, 1)

def find_do(data):
    return re.split(r'do\(\)', data, 1)


if __name__ == '__main__':
    answer1 = 0
    answer2 = 0
    disabled = False
    f = open("day3/example2", "r")
    data = f.read()
    mul_instructions = extract_mul_instructions(data)
    answer1 = compute_mul_instructions(mul_instructions)

    parsed_dont = re.split(r'don\'t', data, 1)

    while True:
       
        parsed_dont = find_dont(data)
        enabled_data = parsed_dont[0]
        disabled_data = parsed_dont[-1]

        print(f"Enabled data are {enabled_data}\n")
        mul_instructions = extract_mul_instructions(enabled_data)
        answer2 = answer2 + compute_mul_instructions(mul_instructions)

        parsed_do = find_do(disabled_data)
        data = parsed_do[-1]

        if enabled_data == disabled_data:
            break


    print(f"Solution for first part is {answer1}")
    print(f"Solution for second part is {answer2}")

