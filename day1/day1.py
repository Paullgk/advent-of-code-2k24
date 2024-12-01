import numpy as np

def first_part(first_col, second_col):
    distance = 0
    total_distance = 0

    while len(first_col) != 0:
        min_first_col = np.min(first_col)
        min_first_col_index = np.argmin(first_col)
        min_second_col = np.min(second_col)
        min_second_col_index = np.argmin(second_col)

        distance = abs(min_first_col - min_second_col)
        total_distance = total_distance + distance
        first_col = np.delete(first_col,min_first_col_index)
        second_col = np.delete(second_col,min_second_col_index)
    return total_distance



if __name__ == '__main__':
    data = np.genfromtxt("day1/data", dtype=int, encoding = None, delimiter="   ")
    first_col = data[:,0]
    second_col = data[:,1]

    answer1 = first_part(first_col, second_col)
    print(f"Solution for first part is {answer1}")

