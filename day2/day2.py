import numpy as np


def check_decreasing(report):
    gap = np.diff(report)
    if np.all(gap < 0):
        if np.any(gap < -3):
            return False
        return True
    
def check_increasing(report):
    gap = np.diff(report)
    if np.all(gap > 0):
        if np.any(gap > 3):
            return False
        return True
    
if __name__ == '__main__':
    f = open("day2/data", "r")
    data = f.read().splitlines()
    safe = 0
    for report in data:
        report = list(map(int, report.split()))
        decrease = check_decreasing(report)
        increase = check_increasing(report)

        if decrease  == True or increase == True:
            safe += 1

    print(f"Solution for first part is {safe}")



    