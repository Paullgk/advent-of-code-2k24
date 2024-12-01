import numpy as np

def first_part(first_col, second_col):
    distance = 0
    total_distance = 0

    while len(first_col) != 0:

        min_first_col = search_min_value(first_col)
        min_second_col = search_min_value(second_col)

        distance = abs(min_first_col[1] - min_second_col[1])
        total_distance = total_distance + distance
        first_col = np.delete(first_col,min_first_col[0])
        second_col = np.delete(second_col,min_second_col[0])
    return total_distance


def second_part(first_col, second_col):
    similarity_score = 0

    for first_col_val in first_col:
        second_col_occurrences = search_coeffcient(second_col, first_col_val)
        similarity_score = similarity_score + (first_col_val * second_col_occurrences)
    return similarity_score

def search_min_value(col):
    min = np.min(col)
    min_index = np.argmin(col)
    return int(min_index),int(min)

def search_coeffcient(col, val):
    return np.count_nonzero(col == val)

if __name__ == '__main__':
    data = np.genfromtxt("day1/data", dtype=int, encoding = None, delimiter="   ")
    first_col = data[:,0]
    second_col = data[:,1]

    answer1 = first_part(first_col, second_col)
    print(f"Solution for first part is {answer1}")

    answer2 = second_part(first_col, second_col)
    print(f"Solution for first part is {answer2}")
