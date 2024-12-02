import numpy as np


def check_decreasing(gap):
    if np.all(gap < 0):
        if np.any(gap < -3):
            return False
        return True

def check_increasing(gap):
    if np.all(gap > 0):
        if np.any(gap > 3):
            return False
        return True

def check_safety(report):
    gap = np.diff(report)
    decrease = check_decreasing(gap)
    increase = check_increasing(gap)

    if decrease  == True or increase == True:
        return True
    else:
        return False
    
if __name__ == '__main__':
    f = open("day2/data", "r")
    data = f.read().splitlines()
    safe = 0
    for report in data:
        report = list(map(int, report.split()))

        if check_safety(report):
            safe += 1

    print(f"Solution for first part is {safe}")
