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
    answer1 = 0
    answer2 = 0
    for report in data:
        report = list(map(int, report.split()))
        safe = check_safety(report)
        if safe is True:
            answer1 += 1
            answer2 += 1
        if safe is False:
            for level_index in range(0, len(report)):
                modified_report = np.delete(report, level_index)
                safe = check_safety(modified_report)

                if safe is True:
                    print(f"Report {report} is safe by removing {report[level_index]}")
                    answer2 += 1
                    break

    print(f"Solution for first part is {answer1}")
    print(f"Solution for first part is {answer2}")
